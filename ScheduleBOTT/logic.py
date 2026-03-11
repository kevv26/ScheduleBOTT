import discord

schedule_data = {
    "Monday": [
        {"Subject": "Math", "Time": "9:00 AM - 10:00 AM"},
        {"Subject": "Physics", "Time": "10:30 AM - 11:30 AM"},
        {"Subject": "Recess", "Time": "11:30 AM - 12:00 PM"},
        {"Subject": "Chemistry", "Time": "12:00 PM - 1:00 PM"}
    ],
    "Tuesday": [
        {"Subject": "Biology", "Time": "9:00 AM - 10:00 AM"},
        {"Subject": "History", "Time": "10:30 AM - 11:30 AM"},
        {"Subject": "Recess", "Time": "11:30 AM - 12:00 PM"},
        {"Subject": "Literature", "Time": "12:00 PM - 1:00 PM"}
    ],
    "Wednesday": [
        {"Subject": "Computer Science", "Time": "9:00 AM - 10:00 AM"},
        {"Subject": "Art", "Time": "10:30 AM - 11:30 AM"},
        {"Subject": "Recess", "Time": "11:30 AM - 12:00 PM"},
        {"Subject": "Physical Education", "Time": "12:00 PM - 1:00 PM"}
    ],
    "Thursday": [
        {"Subject": "Music", "Time": "9:00 AM - 10:00 AM"},
        {"Subject": "Geography", "Time": "10:30 AM - 11:30 AM"},
        {"Subject": "Recess", "Time": "11:30 AM - 12:00 PM"},
        {"Subject": "Economics", "Time": "12:00 PM - 1:00 PM"}
    ],
    "Friday": [
        {"Subject": "Philosophy", "Time": "9:00 AM - 10:00 AM"},
        {"Subject": "Sociology", "Time": "10:30 AM - 11:30 AM"},
        {"Subject": "Recess", "Time": "11:30 AM - 12:00 PM"},
        {"Subject": "Psychology", "Time": "12:00 PM - 1:00 PM"}
    ]
}

def format_schedule(day):
    schedule = ("Schedule for " + day + ":\n")
    for item in schedule_data[day]:
        subject = item["Subject"]
        time = item["Time"]
        schedule += (subject + " = " + time + "\n")
    return schedule

class ScheduleButton(discord.ui.View):
    @discord.ui.button(label="Monday", style=discord.ButtonStyle.primary)
    async def Monday(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(format_schedule("Monday"))

    @discord.ui.button(label="Tuesday", style=discord.ButtonStyle.primary)
    async def Tuesday(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(format_schedule("Tuesday"))

    @discord.ui.button(label="Wednesday", style=discord.ButtonStyle.primary)
    async def Wednesday(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(format_schedule("Wednesday"))

    @discord.ui.button(label="Thursday", style=discord.ButtonStyle.primary)
    async def Thursday(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(format_schedule("Thursday"))

    @discord.ui.button(label="Friday", style=discord.ButtonStyle.primary)
    async def Friday(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(format_schedule("Friday"))