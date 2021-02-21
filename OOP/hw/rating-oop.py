

class Rating:

    def __init__(self, thumbsUp, thumbsDown):
        self.thumbsUp = thumbsUp
        self.thumbsDown = thumbsDown

    def __str__(self):
        return "Rating: 👍" + str(self.thumbsUp) + "  👎" + str(self.thumbsDown)

    def __gt__(self, other):  # greater/ mai mare
        if self.thumbsUp - self.thumbsDown > other.thumbsUp - other.thumbsDown:
            return "Difference between LIKES and DISLIKES is predominate in video_1"
        else:
            return "Difference between LIKES and DISLIKES is predominate in video_2"

    def __lt__(self, other):
        if self.thumbsUp - self.thumbsDown < other.thumbsUp - other.thumbsDown:
            return "video_1_rating is less popular than video_2_rating"
        else:
            return "video_2_rating is less popular than video_1_rating"

    # def __LE__(SELF, OTHER):
    #     if int(SELF.thumbsUp + SELF.thumbsDown) <= int(OTHER.thumbsUp + OTHER.thumbsDown):
    #         return "video_1_rating is less or same mentioned than video_2_rating"
    #     else:
    #         return "video_2_rating is less or same mentioned than video_1_rating"

    def __eq__(self, other):
        if(self.thumbsUp == other.thumbsUp):
            return "Both are equal LIKES"
        else:
            return "Not equal LIKES"



video_1_rating = Rating(1000, 10)
video_2_rating = Rating(9999, 100)


# if video_1_rating > video_2_rating:
#     print("First video is better!!")
# else:
#     print("Second video is better!!")

# print(video_1_rating)    # __str__
# print(video_2_rating)    # __str__

print(video_1_rating > video_2_rating)   # __gt__   >

print(video_1_rating < video_2_rating)   # __lt__   <

# print(video_1_rating <= video_2_rating)   # __LE__   <=

print(video_1_rating == video_2_rating)  # __eq__   ==



