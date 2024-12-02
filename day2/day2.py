import os

def is_report_safe(report):
    diff = report[1] - report[0]
    statut = 'increasing' if diff > 0 else 'decreasing' 
    is_safe = True     
    for i in range(0, len(report) - 1):
        diff = report[i+1] - report[i]
        distance = abs(diff)
        is_safe = not((statut == 'increasing' and diff < 0) or (statut == 'decreasing' and diff > 0) or distance == 0 or distance > 3)
        if not(is_safe):
                break
    return is_safe

def is_report_safe_with_problem_dampener(report):
    for i in range(len(report)):
        copy_report = report.copy()
        del copy_report[i]
        if (is_report_safe(copy_report)):
            return True
    return False

    
    
def main():
    filename = "input_day2.txt"
    if not os.path.isfile(filename) :
        print('Input file does not exist')
    else :
        with open(filename) as f:
            reports = f.read().splitlines() # readlines appends \n in last items
            reports = [list(map(int,report.split())) for report in reports]
            # part 1
            evaluations = [is_report_safe(report) for report in reports]
            nb_safe_reports = sum(evaluations)
            print(f"Part 1 : {nb_safe_reports} safe reports!")
            
            # part 2
            evaluations = [is_report_safe(report) or is_report_safe_with_problem_dampener(report) for report in reports]
            nb_safe_reports = sum(evaluations)
            print(f"Part 2 : {nb_safe_reports} safe reports with the Problem Dampener!")
                    
                     

if __name__ == "__main__":
    main()