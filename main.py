def calculate_dynamic_bitrate(upload_speed_mbps):
    # Convert upload speed to kbps
    upload_speed_kbps = upload_speed_mbps * 1000
    
    # Apply utilization factor (75% for stability)
    safe_bitrate = upload_speed_kbps * 0.75

    # Standard resolutions and frame rates
    resolutions = {
        "480p": (854, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "1440p (2K)": (2560, 1440),
        "2160p (4K)": (3840, 2160),
        "4320p (8K)": (7680, 4320)
    }
    
    frame_rates = [24, 30, 60, 120, 144, 240]

    # Base bitrate per pixel per second (approximation)
    base_bitrate_per_pixel = 0.07  # Approximate factor (can be adjusted)

    results = {}

    for res, (width, height) in resolutions.items():
        for fps in frame_rates:
            # Calculate required bitrate
            pixel_count = width * height
            estimated_bitrate = int(pixel_count * fps * base_bitrate_per_pixel / 1000)  # Convert to kbps
            
            if safe_bitrate >= estimated_bitrate:
                results[f"{res} {fps}fps"] = estimated_bitrate  # Use calculated bitrate
            else:
                results[f"{res} {fps}fps"] = "Insufficient bandwidth"

    return results

# Example usage
upload_speed = 201.07  # Mbps
bitrate_recommendations = calculate_dynamic_bitrate(upload_speed)

# Display the results
for res, bitrate in bitrate_recommendations.items():
    print(f"{res}: {bitrate} kbps")
