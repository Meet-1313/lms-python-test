def summarize_lesson(lesson_text, num_sentences=2):
    """
    Returns a first 'num_sentences' of the lesson as a summary.
    """

    sentences = lesson_text.split('. ')
    summary = '.'.join(sentences[:num_sentences])
    return summary 
if __name__ == "__main__":
    lesson = """python is a versatile programming language . it is widely used in web develoment,data science,ai and more
    Learning python can opne many opporttunitites 
    this script create simple summary of lessons"""


    summary = summarize_lesson(lesson)
    print("Lesson Summary:")
    print (summary)