use std::fs;

fn main() {
    let file = "input.txt";
    let filename = format!("./{}", file);
    let binding = fs::read_to_string(filename).expect("Something went wrong reading the file");

    let contents = binding.trim().split("\n").collect::<Vec<&str>>();

    let mut list_1 = Vec::new();
    let mut list_2 = Vec::new();

    for i in 0..contents.len() {
        let t = contents[i].split("   ").collect::<Vec<&str>>();
        list_1.push(t[0].parse::<i32>().unwrap());
        list_2.push(t[1].parse::<i32>().unwrap());
    }

    let mut result = 0;
    for i in 0..list_1.len() {
        result += list_1[i] * list_2.iter().filter(|&x| x == &list_1[i]).count() as i32;
    }

    println!("Result: {:?}", result);
}
