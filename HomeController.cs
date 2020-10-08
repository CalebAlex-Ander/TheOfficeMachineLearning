using Microsoft.AspNetCore.Mvc;
using Lai_Anna_HW0.Models;
using System.Linq;
using System.Collections.Generic;
using System.Threading;

using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Text.Json;

namespace Lai_Anna_HW0.Controllers
{
    public class HomeController : Controller
    {
        /*static HttpClient client = new HttpClient();
        static async Task<string> RunAsync(data data)
        {
            client.BaseAddress = new Uri("http://localhost:64195/");
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));

            var myObject = JsonSerializer.Serialize(data);


            HttpResponseMessage response = await client.PostAsync("http://localhost:5000/", new StringContent(myObject));
            string helloworld = await response.Content.ReadAsStringAsync();
            return helloworld;
        }*/

        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        public ViewResult Casting()
        {
            return View();
        }

        /*
        [HttpPost]
        public IActionResult Casting(GuestResponse guestResponse)
        {
            if (ModelState.IsValid)
            {
                Repository.AddResponse(guestResponse);
                IEnumerable<GuestResponse> attendeeList = Repository.Responses;
                return View("ListResponses", attendeeList);
            }
            else
            {
                return View();
            }
        }*/

        /*public IActionResult Results()
        {
            data data = new data();
            data.Hello = "Hello World!";
            string result = RunAsync(data).GetAwaiter().GetResult();
            return View("Results", result);
        }*/

        [HttpPost]
        public IActionResult Casting(GuestResponse guestResponse)
        {
            return View("Results", guestResponse);
        }
    }
}







// IEnumerable<GuestResponse> attendeeList = Repository.Responses.Where(r => r.WillAttend == true);
/*public IActionResult ListResponses()
            {
                IEnumerable<GuestResponse> attendeeList = Repository.Responses;
                return View(attendeeList);
            }*/
