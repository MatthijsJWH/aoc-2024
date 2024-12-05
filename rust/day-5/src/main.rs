use std::cmp::Ordering;
use std::collections::HashMap;
use std::fs;
use std::time::Instant;

fn read_input(filename: &str) -> Vec<String> {
    fs::read_to_string(filename)
        .expect("Failed to read file")
        .lines()
        .map(|line| line.parse().unwrap())
        .collect()
}

fn parse_input(contents: &Vec<String>) -> (HashMap<i32, Vec<i32>>, Vec<Vec<i32>>) {
    let mut ordering_rules = HashMap::new();
    let mut updates = vec![];
    for c in contents.iter() {
        if c.len() == 0 {
            continue;
        }

        if c.contains("|") {
            let temp = c
                .split("|")
                .map(|s| s.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();

            if !ordering_rules.contains_key(&temp[0]) {
                ordering_rules.insert(temp[0], vec![temp[1]]);
            } else {
                ordering_rules.get_mut(&temp[0]).unwrap().push(temp[1]);
            }
        } else {
            let temp = c
                .split(",")
                .map(|s| s.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            updates.push(temp);
        }
    }
    (ordering_rules, updates)
}

fn is_valid_update(ordering_rules: &HashMap<i32, Vec<i32>>, update: &Vec<i32>) -> bool {
    for i in 0..update.len() - 1 {
        for j in update[i + 1..].iter() {
            if !ordering_rules.contains_key(j) {
                continue;
            }

            if ordering_rules.get(j).unwrap().contains(&update[i]) {
                return false;
            }
        }
    }
    true
}

fn get_valid_updates(
    ordering_rules: &HashMap<i32, Vec<i32>>,
    updates: &Vec<Vec<i32>>,
) -> Vec<Vec<i32>> {
    let mut valid_updates = vec![];
    for update in updates.iter() {
        if is_valid_update(ordering_rules, update) {
            valid_updates.push(update.clone());
        }
    }
    valid_updates
}

fn count_middle_values(updates: &Vec<Vec<i32>>) -> i32 {
    let mut count = 0;
    for update in updates.iter() {
        let middle_index = update.len() / 2;
        count += update[middle_index];
    }
    count
}

fn order_updates(
    ordering_rules: &HashMap<i32, Vec<i32>>,
    updates: &Vec<Vec<i32>>,
) -> Vec<Vec<i32>> {
    fn compare_entry(x: &i32, y: &i32, ordering_rules: &HashMap<i32, Vec<i32>>) -> Ordering {
        if ordering_rules.contains_key(x) {
            if ordering_rules.get(x).unwrap().contains(y) {
                return Ordering::Less;
            }
        }

        if ordering_rules.contains_key(y) {
            if ordering_rules.get(y).unwrap().contains(x) {
                return Ordering::Greater;
            }
        }

        Ordering::Equal
    }

    let mut ordered_updates = updates.clone();
    for update in ordered_updates.iter_mut() {
        update.sort_by(|a, b| compare_entry(a, b, ordering_rules));
    }
    ordered_updates
}

fn part1(ordering_rules: HashMap<i32, Vec<i32>>, updates: Vec<Vec<i32>>) -> i32 {
    let valid_updates = get_valid_updates(&ordering_rules, &updates);
    count_middle_values(&valid_updates)
}

fn part2(ordering_rules: HashMap<i32, Vec<i32>>, updates: Vec<Vec<i32>>) -> i32 {
    let valid_updates = get_valid_updates(&ordering_rules, &updates);
    let invalid_updates = updates
        .iter()
        .filter(|update| !valid_updates.contains(update))
        .cloned()
        .collect::<Vec<Vec<i32>>>();
    let ordered_updates = order_updates(&ordering_rules, &invalid_updates);
    count_middle_values(&ordered_updates)
}

fn main() {
    let start = Instant::now();

    let file = "input.txt";
    let contents = read_input(file);
    let (ordering_rules, updates) = parse_input(&contents);

    let duration_zero = start.elapsed();
    let part_one = part1(ordering_rules.clone(), updates.clone());
    let duration_one = start.elapsed() - duration_zero;
    let part_two = part2(ordering_rules.clone(), updates.clone());
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
