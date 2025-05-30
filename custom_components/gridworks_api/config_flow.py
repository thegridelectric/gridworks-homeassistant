from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class GridWorksAPIConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the GridWorks API integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Save config entry
            return self.async_create_entry(title="GridWorks API", data=user_input)

        # Show setup form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host"): str,
                vol.Required("api_key"): str,
            })
        )
