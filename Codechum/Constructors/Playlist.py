class Music:
    def __init__(self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
        # Conversion logic based on the duration_type
        if duration_type == 'h':
            # Convert hours to minutes
            self.duration = duration * 60
        elif duration_type == 'd':
            # Convert days to minutes (24 hours * 60 minutes)
            self.duration = duration * 1440
        else:
            # Default to minutes ('m' or anything else)
            self.duration = duration
            
        self.genre = genre