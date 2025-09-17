
from agents import function_tool


@function_tool
async def iphone_battery_status_tool():
    """Returns a detailed mock battery and device status for iPhone."""
    return {
        "device": "iPhone 15 Pro Max",
        "battery_percent": 80,
        "battery_health": "Excellent",
        "charging_status": "Not Charging",
        "last_charged": "2025-09-17T08:00:00Z",
        "temperature_celsius": 32.1,
        "serial_number": "IP15PM-XYZ123456",
        "model_number": "A2651",
        "os_version": "iOS 18.2",
        "storage_total_gb": 256,
        "storage_used_gb": 120.5,
        "storage_free_gb": 135.5,
        "wifi_connected": True,
        "wifi_ssid": "HomeNetwork5G",
        "bluetooth_enabled": True,
        "location_enabled": True,
        "find_my_enabled": True,
        "low_power_mode": False,
        "screen_time_today_min": 210,
        "last_backup": "2025-09-15T23:45:00Z",
        "notes": "Battery is in optimal condition. No issues detected."
    }


@function_tool
async def ipad_screen_size_tool():
    """Returns a detailed mock device and screen info for iPad."""
    return {
        "device": "iPad Pro 11-inch (5th Gen)",
        "screen_size_inches": 11.0,
        "screen_resolution": "2388 x 1668",
        "screen_type": "Liquid Retina",
        "refresh_rate_hz": 120,
        "brightness_nits": 600,
        "battery_percent": 67,
        "os_version": "iPadOS 18.2",
        "serial_number": "IPDP11G5-ABC987654",
        "model_number": "A2459",
        "storage_total_gb": 512,
        "storage_used_gb": 300.2,
        "storage_free_gb": 211.8,
        "wifi_connected": True,
        "wifi_ssid": "OfficeWiFi",
        "bluetooth_enabled": True,
        "apple_pencil_connected": True,
        "face_id_enabled": True,
        "last_backup": "2025-09-16T21:30:00Z",
        "notes": "Screen is in perfect condition. No dead pixels."
    }


@function_tool
async def macbook_storage_tool():
    """Returns a detailed mock storage and device status for MacBook."""
    return {
        "device": "MacBook Pro 16-inch (M3, 2024)",
        "storage_total_gb": 1024,
        "storage_used_gb": 768.3,
        "storage_free_gb": 255.7,
        "disk_type": "Apple SSD AP1024Q",
        "os_version": "macOS 15.1 (Sequoia)",
        "serial_number": "MBP16M3-DEF456789",
        "model_number": "A2780",
        "battery_percent": 92,
        "battery_health": "Good",
        "charging_status": "Charging",
        "wifi_connected": True,
        "wifi_ssid": "CorpNet",
        "bluetooth_enabled": True,
        "touch_id_enabled": True,
        "last_backup": "2025-09-10T18:00:00Z",
        "notes": "SSD health is normal. Storage usage is high."
    }


@function_tool
async def airpods_battery_tool():
    """Returns a detailed mock battery and device status for AirPods."""
    return {
        "device": "AirPods Pro (3rd Gen)",
        "left_airpod_battery": 90,
        "right_airpod_battery": 88,
        "case_battery": 75,
        "noise_cancellation": True,
        "transparency_mode": False,
        "serial_number": "APP3G-HIJ654321",
        "model_number": "A2084",
        "firmware_version": "6A300",
        "connected_device": "iPhone 15 Pro Max",
        "last_connected": "2025-09-17T07:55:00Z",
        "find_my_enabled": True,
        "notes": "All components are functioning normally."
    }


@function_tool
async def sales_target_tool():
    """Returns a detailed mock sales target and related info."""
    return {
        "device": "Sales Dashboard",
        "sales_target": "$1,000,000",
        "current_sales": "$750,000",
        "target_period": "Q3 2025",
        "top_performer": "Jane Doe",
        "top_region": "APAC",
        "number_of_deals": 42,
        "average_deal_size": "$17,857",
        "pipeline_value": "$300,000",
        "win_rate_percent": 38.5,
        "last_updated": "2025-09-17T08:10:00Z",
        "notes": "On track to meet target. Focus on closing high-value deals in EMEA."
    }



# iPhone tools
@function_tool
def iphone_ios_version_tool():
    """Returns the current iOS version of the iPhone."""
    return "iOS 17.0.1"

@function_tool
def iphone_camera_specs_tool():
    """Returns the camera specifications of the iPhone."""
    return "12MP Ultra Wide and Wide cameras"

# iPad tools
@function_tool
def ipad_pencil_compatibility_tool():
    """Returns Apple Pencil compatibility for the iPad."""
    return "Compatible with Apple Pencil (2nd generation)"

@function_tool
def ipad_storage_info_tool():
    """Returns the storage information of the iPad."""
    return "128GB available"

# MacBook tools
@function_tool
def macbook_ram_size_tool():
    """Returns the RAM size of the MacBook."""
    return "16GB RAM"

@function_tool
def macbook_macos_version_tool():
    """Returns the macOS version of the MacBook."""
    return "macOS Sonoma 14.0"

# AirPods tools
@function_tool
def airpods_firmware_version_tool():
    """Returns the firmware version of the AirPods."""
    return "Firmware version 6A300"

@function_tool
def airpods_find_location_tool():
    """Returns the last known location of the AirPods."""
    return "Last seen at Home"

# Sales tools
@function_tool
def sales_leaderboard_tool():
    """Returns the current sales leaderboard."""
    return [{"name": "Alice", "sales": 1200000}, {"name": "Bob", "sales": 950000}]

@function_tool
def sales_inventory_tool():
    """Returns the current product inventory status."""
    return {"iPhone": 120, "iPad": 80, "MacBook": 45}
