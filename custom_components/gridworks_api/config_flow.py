from homeassistant import config_entries
from .const import DOMAIN

class GridWorksAPIConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the GridWorks API integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        # Check if the integration was already configured
        for entry in self._async_current_entries():
            if entry.domain == DOMAIN:
                return self.async_abort(reason="already_configured")

        # No config needed, create entry immediately
        return self.async_create_entry(title="GridWorks API", data={})
