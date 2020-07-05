fn main() {
    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().to_owned()
    };

    let a2 = s.chars().nth(2).unwrap() == s.chars().nth(3).unwrap();
    let a3 = s.chars().nth(4).unwrap() == s.chars().nth(5).unwrap();
    let result = if a2 && a3 {
        "Yes"
    } else {
        "No"
    };
    println!("{}", result)
}
