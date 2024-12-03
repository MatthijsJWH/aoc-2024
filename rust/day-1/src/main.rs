use std::fs;
use std::time::Instant;

fn read_input() -> Vec<String> {
    let file = "input.txt";
    let filename = format!("./{}", file);
    let binding = fs::read_to_string(filename).expect("Something went wrong reading the file");

    binding.trim().split("\n").map(|s| s.to_string()).collect()
}

fn parse_input(input: Vec<String>) -> (Vec<i32>, Vec<i32>) {
    let mut list_1 = Vec::new();
    let mut list_2 = Vec::new();

    for i in input.iter() {
        let t = i.split("   ").collect::<Vec<&str>>();
        list_1.push(t[0].parse::<i32>().unwrap());
        list_2.push(t[1].parse::<i32>().unwrap());
    }

    (list_1, list_2)
}

fn part_1(mut list_1: Vec<i32>, mut list_2: Vec<i32>) -> i32 {
    let mut result = 0;
    list_1.sort();
    list_2.sort();
    for i in 0..list_1.len() {
        result += (list_1[i] - list_2[i]).abs();
    }

    result
}

fn part_2(list_1: Vec<i32>, list_2: Vec<i32>) -> i32 {
    let mut result = 0;

    for num in list_1.iter() {
        result += num * list_2.iter().filter(|&x| x == num).count() as i32;
    }

    result
}

fn main() {
    let start = Instant::now();
    let input = read_input();
    let (list_1, list_2) = parse_input(input);

    let duration_zero = start.elapsed();
    let part_one = part_1(list_1.clone(), list_2.clone());
    let duration_one = start.elapsed() - duration_zero;
    let part_two = part_2(list_1.clone(), list_2.clone());
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
