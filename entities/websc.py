import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class XPathexample {
public static void main(String[] args) {
System.setProperty("webdriver.chrome.driver", "Your-Chrome-Driver-Path"); // Provide the path to your chrome driver. Make sure your chrome driver version is updated.
WebDriver driver = new ChromeDriver();
driver.manage().window().maximize();
driver.manage().deleteAllCookies();
driver.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
driver.get("https://login.yahoo.com/account/create");
driver.findElement(By.xpath("//input[@id='usernamereg-firstName']")).sendKeys("Your-Name");