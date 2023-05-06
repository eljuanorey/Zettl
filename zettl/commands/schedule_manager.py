from zettl import *

class ReviewIntervals:
    
    INTERVALS = {
        "1 day": 1,
        "1 week": 7,
        "1 month": 30
    }

    @classmethod
    def get_days(cls, interval):
        return cls.INTERVALS.get(interval, None)

        
def create_review_schedule(folder_paths):
    
    review_schedule = []
    now = datetime.now()
    
    for folder_path in folder_paths:
        try:
            for filename in os.listdir(folder_path):
                
                if filename.endswith(".md"):
                    
                    file_path = os.path.join(folder_path, filename)
                    creation_date = datetime.fromtimestamp(os.path.getctime(file_path))
                    
                    for interval in ReviewIntervals.INTERVALS.keys():
                        if creation_date + timedelta(days=ReviewIntervals.get_days(interval)) > now:
                            days_left = ((creation_date + timedelta(days=ReviewIntervals.get_days(interval))) - now).days
                            review_schedule.append((filename, creation_date + timedelta(days=ReviewIntervals.get_days(interval)) , interval, days_left))
        except FileNotFoundError:
            print(f"Folder path not found: {folder_path}")

    return review_schedule


def copy_files(review_schedule, folder_paths, copy_to_folder):
    
    if not os.path.exists(copy_to_folder):
        os.makedirs(copy_to_folder)
        
    for folder_path in folder_paths:
        for filename, next_review_date, interval, days_left in review_schedule:
            try:
                if days_left == 0:
                    source_file = os.path.join(folder_path, filename)
                    dest_file = os.path.join(copy_to_folder, filename)
                    shutil.copyfile(source_file, dest_file)
            except FileNotFoundError:
                pass


def save_review_schedule(review_schedule, save_to_folder, file_name):
    
    review_schedule = sorted(review_schedule, key=lambda x: x[1])
    
    with open(os.path.join(save_to_folder, file_name), "w") as f:
        f.write("| File | Review Date | Interval | Days Left |\n")
        f.write("|------|-------------|----------|----------|\n")
        for filename, next_review_date, interval, days_left in review_schedule:
            f.write(f"| {filename} | {next_review_date.strftime('%Y-%m-%d')} | {interval} | {days_left} |\n")