import * as dateFns from "https://unpkg.com/date-fns?module"

const eventList = [
    {
        startDate: "10/1/2020 10:00 AM",
        endDate: "10/1/2020 12:00 PM",
        allDay: false,
        title: "Lorem ipsum dolor sit amet",
        description: "Lorem ipsum dolor sit amet"
    },
    {
        startDate: "10/3/2020 00:00 AM",
        endDate: "10/4/2020 00:00 AM",
        allDay: true,
        title: "Lorem ipsum dolor sit amet",
        description: "Lorem ipsum dolor sit amet"
    },
    {
        startDate: "10/9/2020 10:30 AM",
        endDate: "10/9/2020 11:00 AM",
        allDay: false,
        title: "Lorem ipsum dolor sit amet",
        description: "Lorem ipsum dolor sit amet"
    },
    {
        startDate: "10/13/2020 10:00 AM",
        endDate: "10/13/2020 12:00 PM",
        allDay: false,
        title: "Lorem ipsum dolor sit amet",
        description: "Lorem ipsum dolor sit amet"
    },
    {
        startDate: "4/3/2020 2:00 PM",
        endDate: "4/3/2020 6:00 PM",
        allDay: false,
        title: "Lorem ipsum dolor sit amet",
        description: "Lorem ipsum dolor sit amet"
    },
    {
        startDate: "10/10/2020 11:00 AM",
        endDate: "10/10/2020 3:00 PM",
        allDay: false,
        title: "스쿼트 10개",
        description: "스쿼트 10개"
    },
    {
        startDate: "10/10/2020 3:15 PM",
        endDate: "10/10/2020 5:20 PM",
        allDay: false,
        title: "스쿼트 10개",
        description: "스쿼트 10개"
    },
    {
        startDate: "10/10/2020 9:00 AM",
        endDate: "10/10/2020 10:30 AM",
        allDay: false,
        title: "스쿼트 15개",
        description: "스쿼트 10개"
    }
];

Vue.component("Calendar", {
    delimiters: ['[[', ']]'],
    template: "#calendar-template",
    name: "Calendar",
    data() {
        return {
            currentMonth: new Date(),
            selectedDate: new Date(),
            events: eventList,
            transitionDirection: "",
            currentPage: {
                month: dateFns.getMonth(new Date()),
                year: dateFns.getYear(new Date())
            }
        };
    },
    watch: {
    currentPage(val, oldVal) {
      this.transitionDirection = this.getTransitionDirection(oldVal, val);
    }
    },
    methods: {
        nextMonth() {
      this.currentMonth = dateFns.addMonths(this.currentMonth, 1);
      this.updateCurrentPage(this.currentMonth);
    },

    prevMonth() {
      this.currentMonth = dateFns.subMonths(this.currentMonth, 1);
      this.updateCurrentPage(this.currentMonth);
    },

    updateDate(day) {
      this.selectedDate = day.day;
    },

    updateCurrentPage(date) {
      this.currentPage = {
        month: dateFns.getMonth(date),
        year: dateFns.getYear(date)
      };
    },

        findEvents(day, sort = false) {
            let hasEvents = this.events.reduce((list, ev) => {
                if (dateFns.isSameDay(day, new Date(ev.startDate))) {
                    ev.isActive =
                        ev.allDay ||
                        dateFns.isWithinInterval(
                            new Date(),
                            { start:new Date(ev.startDate), end:new Date(ev.endDate)}
                        );
                    list.push(ev);
                }
                return list;
            }, []);
            if (sort) {
                hasEvents.sort((a, b) => {
                    const dateA = new Date(a.startDate);
                    const dateB = new Date(b.startDate);
                    return dateFns.compareAsc(dateA, dateB);
                });
            }
            return hasEvents;
        },

        getTransitionDirection(fromPage, toPage) {
            if (!fromPage || !toPage) return "";
            if (fromPage.year !== toPage.year)
                return fromPage.year < toPage.year ? "next" : "prev";
            if (fromPage.month !== toPage.month)
                return fromPage.month < toPage.month ? "next" : "prev";
            return "";
        }
    },
    computed: {
        selectedDay() {
            return {
                number: dateFns.format(this.selectedDate, "d"),
                name: dateFns.format(this.selectedDate, "cccc")
                //name: dateFns.format(this.selectedDate, "dddd")
            };
        },

        month() {
            const dateFormat = "MMMM yyyy";
            return dateFns.format(this.currentMonth, dateFormat);
        },

        dayNames() {
            const dateFormat = "ccc";
            let startDate = dateFns.startOfISOWeek(this.currentMonth);

            const days = [];
            for (let i = 0; i < 7; i += 1) {
                days.push(dateFns.format(dateFns.addDays(startDate, i), dateFormat));
            }
            return days;
        },

        rows() {
            const monthStart = dateFns.startOfMonth(this.currentMonth);
            const monthEnd = dateFns.endOfMonth(monthStart);
            const startDate = dateFns.startOfISOWeek(monthStart);
            const endDate = dateFns.endOfISOWeek(monthEnd);

            const dateFormat = "d";
            const rows = [];

            let days = [];
            let day = startDate;
            let formattedDate = "";

            while (day <= endDate) {
                for (let i = 0; i < 7; i += 1) {
                    formattedDate = dateFns.format(day, dateFormat);
                    const dayInfo = {
                        day,
                        formattedDate,
                        type: !dateFns.isSameMonth(day, monthStart)
                            ? "disabled"
                            : dateFns.isSameDay(day, this.selectedDate) ? "selected" : "",
                        hasEvents: this.findEvents(day).length > 0
                    };
                    days.push(dayInfo);
                    day = dateFns.addDays(day, 1);
                }
                rows.push({ days: days });
                days = [];
            }
            return rows;
        },		
        dayEvents() {
      return this.findEvents(this.selectedDate, true);
    },

    typeTransition() {
      return `${
        this.transitionDirection === "next" ? "slide-left" : "slide-right"
      }`;
    }
    },
    filters: {
        getTime(value) {
            const dateFormat = "h:mm aaa";
            // let strarray = value.split(" ")
            return dateFns.format(new Date(value), dateFormat);
        }
    }
});

var app = new Vue({
	el: "#app"
});
