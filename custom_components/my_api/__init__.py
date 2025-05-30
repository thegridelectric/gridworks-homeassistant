from homeassistant.core import HomeAssistant
from .api import ApiTankModule

async def async_setup(hass: HomeAssistant, config: dict):
    hass.http.register_view(ApiTankModule(hass))
    return True