use regex::Regex;
use std::fs;
use std::time::Instant;

fn read_input(filename: String) -> String {
    let binding = fs::read_to_string(filename).expect("Something went wrong reading the file");

    binding.trim().to_string()
}

fn apply_mul(command: String) -> i32 {
    let mut t = command.split("mul(").collect::<Vec<&str>>();
    t = t[1].split(",").collect::<Vec<&str>>();

    let a = t[0].parse::<i32>().unwrap();

    t = t[1].split(")").collect::<Vec<&str>>();

    let b = t[0].parse::<i32>().unwrap();

    a * b
}

fn part1(input: String) -> i32 {
    let re = Regex::new(r"mul\(\d{1,3},\d{1,3}\)").unwrap();
    let caps = re
        .find_iter(&input)
        .map(|m| m.as_str())
        .collect::<Vec<&str>>();
    let mut result = 0;

    for cap in caps.iter() {
        result += apply_mul(cap.to_string());
    }
    result
}

fn part2(input: String) -> i32 {
    let re = Regex::new(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))").unwrap();
    let caps = re
        .find_iter(&input)
        .map(|m| m.as_str())
        .collect::<Vec<&str>>();

    let mut result = 0;
    let mut do_count = true;

    for cap in caps.iter() {
        match cap.to_string().as_str() {
            "do()" => do_count = true,
            "don't()" => do_count = false,
            _ => {
                if do_count {
                    result += apply_mul(cap.to_string());
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

    let duration_zero = start.elapsed();
    let part_one = part1(contents.clone());
    let duration_one = start.elapsed() - duration_zero;
    let part_two = part2(contents.clone());
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
