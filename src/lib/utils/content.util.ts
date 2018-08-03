export class ContentUtils {
    constructor() {}

    placeholders = [
        "Conquered the world",
        "Met a dog",
        "Met a cat",
        "Ate some cheese",
        "Accomplished all my tasks at work",
        "Made a new friend",
        "Did absolutely fucking nothing, and it was great.",
        "Made a thing",
        "Was pay day",
        "Found some new music",
        "Saw some awesome art",
        "Hung out with some friends",
        "Went on a date",
        "Hung out with my parents",
        "Traveled the world",
        "Drank some coffee",
        "Drank some tea",
        "Ate a new food",
        "Conquered a fear",
        "Hit a major life milestone!!!",
        "Got promoted!",
        "Made someones day",
        "Had my day made!",
        "Went to the zoo",
        "Saw a new movie",
        "Did a thing!",
        "Conquered the thing!",
        "Learned a thing!",
        "Cleaned out my closet",
        "Drank a whole bottle of wine because I'm an adult and I do what I want"
    ]

    getRandomPlaceholder() {
        return this.getFiveRandomThings();
    }

    private getFiveRandomThings() {
        let things = [];
        let tempHolders = this.placeholders;

        for (let i = 0; i < 5; i++) {
            let randomItem = tempHolders[Math.round(Math.random() * (this.placeholders.length - 1))];
            things.push(randomItem);
            tempHolders = tempHolders.filter(item => item !== randomItem);
            console.log(tempHolders.length);
        }

        return things;
    }
}