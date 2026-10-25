import csv, json, pytest
from pathlib import Path


def pytest_generate_tests(metafunc):
    if "product" not in metafunc.fixturenames:
        return

    products_path = Path(__file__).parent / "data" / "products.csv"
    with products_path.open(newline="", encoding="utf-8") as products_file:
        products = [
            row["Products"].strip()
            for row in csv.DictReader(products_file)
            if row["Test"].strip().casefold() == "yes"
            and row["Products"].strip()
        ]

    if not products:
        raise pytest.UsageError(f"No enabled products found in {products_path}")

    metafunc.parametrize("product", products, ids=products)


@pytest.fixture(scope="session")
def script_test_data():
    data_path = Path(__file__).parent / "data" / "testdata.json"
    with data_path.open(encoding="utf-8") as datafile:
        return json.load(datafile)


@pytest.fixture(
    params=[
        pytest.param("qa", id="qa", marks=pytest.mark.smoke),
        # pytest.param("uat", id="uat", marks=pytest.mark.regression),
        # pytest.param("qa", id="qa", marks=pytest.mark.functional),
    ]
)
def environment_config(request, script_test_data):
    environment = request.param
    environment_data = next(
        item[environment] for item in script_test_data if environment in item
    )
    config = environment_data[0]
    credentials = config[f"{environment}_user_credentials"]

    return {
        "environment": environment,
        "url": config[f"{environment}_url"],
        "email": credentials[f"{environment}_user_email"],
        "password": credentials[f"{environment}_user_password"],
    }


@pytest.fixture
def screenshot_dir(environment_config):
    output_dir = Path(__file__).parent / "test-results" / environment_config["environment"]
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection: Chrome default or Edge"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

#@pytest.fixture(scope="session")
@pytest.fixture
def browserInstance(playwright, request):
    base_url = request.config.getini("base_url")
    browser_name= request.config.getoption("browser_name")
    if browser_name=="firefox":
        browser=playwright.firefox.launch(headless=False)
    elif browser_name=="edge":
        browser=playwright.msedge.launch(headless=False)
    else:
        browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(base_url=base_url)
    page=context.new_page()
    yield page
    context.close()
    browser.close()
        
    
