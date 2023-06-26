def main():

    m_perc = input()
    f_perc = input()

    total = float(m_perc) + float(f_perc)

    print("The total number of students:   \t" + format(total, '.0f' ))
    print(f"The number of males and females \t{m_perc}      \t{f_perc}")
    temp1 = m_perc
    temp2 = f_perc

    ### 40 / 100 is fraction value. It is not a percentage. To get a percentage value, you should time by 100
    m_perc = float(m_perc)/total * 100
    f_perc = float(f_perc)/total * 100
    print(f"The percentage of males and females     {format((m_perc), '.2%')}          {format((f_perc), '.2%')}")

    ### Question. Why do you assign "temp1" to m_perc even "m_perc" has the correct value now?
    
    ## temp1 is the string data type
    # When you assign it to m_perc, m_perc has the string value
    # But, you should return floating values
    # The below two lines should be deleted.
    # m_perc = temp1
    # f_perc = temp2
    return m_perc, f_perc



if __name__ == '__main__':
    main()
