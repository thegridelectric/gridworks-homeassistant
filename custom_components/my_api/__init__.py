from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .api import ApiTankModule

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.http.register_view(ApiTankModule(hass))
    return True