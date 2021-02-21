

class Rating:

    def __init__(self, thumbsUp, thumbsDown):
        self.thumbsUp = thumbsUp
        self.thumbsDown = thumbsDown

    def __str__(self):
        return "Rating: 👍" + str(self.thumbsUp) + "  👎" + str(self.thumbsDown)

    def __gt__(self, other): # greater/ mai mare
        return self.thumbsUp - self.thumbsDown > other.thumbsUp - other.thumbsDown




video_1_rating = Rating(1000, 10)
video_2_rating = Rating(9999, 100)


if video_1_rating > video_2_rating:
    print("First video is better!!")
else:
    print("Second video is better!!")


print(video_1_rating)
print(video_2_rating)