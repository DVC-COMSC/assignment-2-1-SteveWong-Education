def main():

    m_perc = input()
    f_perc = input()

    total = float(m_perc) + float(f_perc)

    print("The total number of students:   \t" + format(total, '.0f' ))
    print(f"The number of males and females \t{m_perc}      \t{f_perc}")
    
    temp1 = float(m_perc)/total 
    temp2 = float(f_perc)/total 
    print(f"The percentage of males and females     {format((temp1), '.2%')}          {format((temp2), '.2%')}")

    m_perc = float(temp1)*100
    f_perc = float(temp2)*100
    return m_perc, f_perc



if __name__ == '__main__':
    main()
