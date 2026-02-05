import re
from typing import Any, Dict


class JsonPreprocessor:
    """
    A helper class to clean and prepare JSON-like data.
     It can:
    - Make all dictionary keys clean and consistent
      (lowercase, no extra spaces, no special characters)
    - Remove keys and values that are None

    This is useful when working with messy data from APIs or users.
    """

    def normalize_keys(self, json_obj: Any) -> Any:
        """
        Cleans dictionary keys by:
        - converting them to lowercase
        - removing extra spaces
        - replacing spaces and dashes with underscores
        """

        def _normalize_key(key: Any) -> str:
            # Convert key to string, remove extra spaces, and make it lowercase
            key_str = str(key).strip().lower()

            # Replace spaces and hyphens with underscores
            key_str = re.sub(r"[ -]+", "_", key_str)

            # Remove multiple underscores and keep only one
            key_str = re.sub(r"_+", "_", key_str)

            return key_str

        # If the input is a dictionary
        if isinstance(json_obj, dict):
            normalized: Dict[str, Any] = {}

            # Loop through each key-value pair
            for key, value in json_obj.items():
                # Normalize the key and apply the same logic to the value
                normalized[_normalize_key(key)] = self.normalize_keys(value)

            return normalized

        # If the input is a list
        if isinstance(json_obj, list):
            # Apply normalization to each item in the list
            return [self.normalize_keys(item) for item in json_obj]

        # If it's not a dict or list, return it as it is
        return json_obj

    def strip_nulls(self, json_obj: Any) -> Any:
        """
        Removes all None values from dictionaries and lists.
        """

        # If the input is a dictionary
        if isinstance(json_obj, dict):
            cleaned: Dict[Any, Any] = {}

            # Loop through each key-value pair
            for key, value in json_obj.items():
                # Keep only values that are not None
                if value is not None:
                    cleaned[key] = self.strip_nulls(value)

            return cleaned

        # If the input is a list
        if isinstance(json_obj, list):
            # Remove None values and clean remaining items
            return [self.strip_nulls(item) for item in json_obj if item is not None]

        # Return the value if it's not a dict or list
        return json_obj


# ---------- Sample input data ----------
# This JSON contains extra spaces, mixed cases, dashes, and None values
data = {
    " User Name ": "Alice",
    "Age": None,
    "Phone-Number": "12345",
    "Details": {
        "City Name": "NY",
        "Zip": None
    },
    "Tags": [None, "Admin", "User"]
}

# ---------- Processing ----------
# Create an object of the JsonPreprocessor class
processor = JsonPreprocessor()

# First normalize the keys, then remove None values
result = processor.strip_nulls(processor.normalize_keys(data))

# ---------- Output ----------
# Print the final cleaned JSON
print(result)
