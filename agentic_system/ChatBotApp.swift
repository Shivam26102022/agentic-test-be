import SwiftUI

struct Message: Identifiable, Codable {
    let id = UUID()
    let text: String
    let isUser: Bool
}

class ChatViewModel: ObservableObject {
    @Published var messages: [Message] = []
    @Published var inputText: String = ""
    
    let backendURL = "https://your-backend-url.com/api/chat" // Change to your backend endpoint
    
    func sendMessage() {
        let userMessage = Message(text: inputText, isUser: true)
        messages.append(userMessage)
        let input = inputText
        inputText = ""
        
        // Prepare request
        guard let url = URL(string: backendURL) else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        let body = ["message": input]
        request.httpBody = try? JSONEncoder().encode(body)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else { return }
            if let reply = try? JSONDecoder().decode([String: String].self, from: data),
               let botReply = reply["reply"] {
                DispatchQueue.main.async {
                    self.messages.append(Message(text: botReply, isUser: false))
                }
            }
        }.resume()
    }
}

struct ChatView: View {
    @ObservedObject var viewModel = ChatViewModel()
    
    var body: some View {
        VStack {
            ScrollView {
                ForEach(viewModel.messages) { message in
                    HStack {
                        if message.isUser {
                            Spacer()
                            Text(message.text)
                                .padding()
                                .background(Color.blue.opacity(0.7))
                                .foregroundColor(.white)
                                .cornerRadius(10)
                        } else {
                            Text(message.text)
                                .padding()
                                .background(Color.gray.opacity(0.2))
                                .foregroundColor(.black)
                                .cornerRadius(10)
                            Spacer()
                        }
                    }.padding(.horizontal)
                }
            }
            HStack {
                TextField("Type a message...", text: $viewModel.inputText)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                Button(action: {
                    viewModel.sendMessage()
                }) {
                    Image(systemName: "paperplane.fill")
                        .foregroundColor(.blue)
                }
                .disabled(viewModel.inputText.isEmpty)
            }
            .padding()
        }
    }
}

@main
struct ChatBotApp: App {
    var body: some Scene {
        WindowGroup {
            ChatView()
        }
    }
}
