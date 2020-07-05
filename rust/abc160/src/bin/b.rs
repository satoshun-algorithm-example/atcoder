fn main() {
    let mut x = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().to_owned().parse::<i32>().unwrap()
    };

    let mut result = 0;

    result += (x / 500) * 1000;
    x = x % 500;

    result += (x / 5) * 5;

    println!("{}", result);
}
