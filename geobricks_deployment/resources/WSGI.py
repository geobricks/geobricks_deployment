from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge
from geobricks_common_settings import settings_app
from geobricks_rest_settings import settings_rest_modules

# loading settings
common_settings["settings"] = dict_merge(common_settings, settings_app)
common_settings["settings"] = common_settings["settings"]["settings"]

# loading  modules
rest_settings["modules"] = dict_merge(rest_settings, settings_rest_modules)
rest_settings["modules"] = rest_settings["modules"]["modules"]

# load app
from geobricks_rest_engine.rest.engine import app
if __name__ == "__main__":
    app.run()
