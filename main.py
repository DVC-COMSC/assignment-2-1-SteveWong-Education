def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_perc = input()
    f_perc = input()

    total = float(m_perc) + float(f_perc)
    
    print("The total number of students:   \t" + format(total, '.0f' ))
    print(f"The number of males and females \t{m_perc}      \t{f_perc}")
    m_perc = float(m_perc)/100
    f_perc = float(f_perc)/100
    print(f"The percentage of males and females     {format((m_perc), '.2%')}          {format((f_perc), '.2%')}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
