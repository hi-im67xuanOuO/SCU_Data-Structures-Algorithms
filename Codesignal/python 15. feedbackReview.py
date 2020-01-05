import textwrap

def feedbackReview(feedback, size):
    # given a feedback and the size of the screen, splits the feedback into lines
    # For feedback = "This is an example feedback" and size = 8, the output should be 
    # feedbackReview(feedback, size) = ["This is", 
    #                                   "an", 
    #                                   "example", 
    #                                   "feedback
    
    return [] if feedback == "" else textwrap.fill(feedback, width=size).split('\n')
