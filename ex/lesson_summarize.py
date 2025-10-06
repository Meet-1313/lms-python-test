def summarize_lesson(lesson_text, num_sentences=2):
    """
    Returns a first 'num_sentences' of the lesson as a summary.
    """

    sentences = lesson_text.split('. ')
    summary = '.'.join(sentences[:num_sentences])
    return summary 
if __name__ == "__main__":
    lesson = input ("enter your leeson text: ")
    summary = summarize_lesson(lesson)
    print("Lesson Summary:")
    print (summary)