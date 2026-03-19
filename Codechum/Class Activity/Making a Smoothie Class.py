class Blender:
    def blend(self, fruit1: str = None, fruit2: str = None, n: int = 1):
        # 1. Check if both fruits are missing
        if fruit1 is None and fruit2 is None:
            message = "There's nothing to blend here, boss."
        else:
            # 2. If fruits are provided, format the string
            message = f"Blending {fruit1} and {fruit2}, boss."
        
        # 3. Repeat the message n times
        for _ in range(n):
            print(message)