from streamlit import markdown


def customStyle():
    markdown(
        """
        <style>
        div[data-testid="collapsedControl"]
        {
            display: none !important;
        }

        footer {visibility: hidden;}


        </style>


    """, unsafe_allow_html=True)


def humanbytes(B):
    """ Return a human-readable string representation of bytes
    Source: https://stackoverflow.com/a/31631711

    Args:
        B (int): Bytes

    Returns:
        str: Human-readable string representation of bytes
    """
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)
