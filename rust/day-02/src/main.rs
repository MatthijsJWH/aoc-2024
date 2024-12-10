use std::fs;
use std::time::Instant;

fn read_input(filename: String) -> Vec<String> {
    let binding = fs::read_to_string(filename).expect("Something went wrong reading the file");

    binding.trim().split("\n").map(|s| s.to_string()).collect()
}

fn parse_input(contents: &Vec<String>) -> Vec<Vec<i32>> {
    let mut list = Vec::new();
    for c in contents.iter() {
        let t = c
            .split(" ")
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        list.push(t);
    }
    list
}

fn check_safe(report: &Vec<i32>, asc: bool) -> bool {
    for i in 0..report.len() {
        if i == report.len() - 1 {
            break;
        }

        let mut diff = report[i] - report[i + 1];
        if asc && diff > 0 {
            return false;
        }

        if !asc && diff < 0 {
            return false;
        }
        diff = diff.abs();
        if diff == 0 || diff > 3 {
            return false;
        }
    }
    return true;
}

fn part1(parsed: Vec<Vec<i32>>) -> i32 {
    let mut result = 0;
    for report in parsed.iter() {
        if check_safe(report, report[0] < report[1]) {
            result += 1;
        }
    }
    result
}

fn part2(parsed: Vec<Vec<i32>>) -> i32 {
    let mut result = 0;
    for report in parsed.iter() {
        if check_safe(report, report[0] < report[1]) {
            result += 1;
        } else {
            for i in 0..report.len() {
                let mut r = report.clone();
                r.remove(i);
                if check_safe(&r, r[0] < r[1]) {
                    result += 1;
                    break;
                }
            }
        }
    }
    result
}

fn main() {
    let start = Instant::now();

    let file = "input.txt";
    let filename = format!("./{}", file);
    let contents = read_input(filename);
    let parsed = parse_input(&contents);

    let duration_zero = start.elapsed();
    let part_one = part1(parsed.clone());
    let duration_one = start.elapsed() - duration_zero;
    let part_two = part2(parsed.clone());
    let duration_two = start.elapsed() - duration_one;

    println!("Time Elapsed While Parsing: {:?}", start.elapsed());
    println!(
        "Result Part 1: {:?}, Time Elapsed: {:?}",
        part_one, duration_one
    );
    println!(
        "Result Part 2: {:?}, Time Elapsed: {:?}",
        part_two, duration_two
    );
}
