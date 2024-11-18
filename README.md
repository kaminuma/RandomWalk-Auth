# RandomWalk-Auth

## Overview
RandomWalk-Auth is a proof-of-concept authentication system that explores the use of random walks as an alternative method for user authentication. This project is designed to provide a flexible and secure approach to authentication, independent of traditional password-based methods. By leveraging a user-provided seed, it generates a sequence of movements that can be used for secure verification.

## Theoretical Background
The concept behind RandomWalk-Auth is to utilize a **random walk** based on a user-provided seed for authentication. The idea is to allow a secure, challenge-response style verification without the need for storing sensitive user information on the server.

1. **Seed-Based Random Walk Generation**:
    - A seed is used to generate an initial coordinate `(x0, y0)` on the client-side. This initial coordinate remains unknown to the server.
    - From this initial point, the system generates a sequence of movements (up, down, left, right, or stay) based on the given number of steps. The step count is flexible and can be adjusted based on security requirements.

2. **Challenge-Response Authentication**:
    - The frontend retains the full coordinate sequence generated from the seed, while the server only stores the sequence of movements.
    - During the authentication process, the server issues a set of random challenges (e.g., "What is the direction at step n and n+1?"), and the user responds with the corresponding steps from their locally generated sequence.
    - The server verifies the user's response to confirm their identity.

## Current Prototype Implementation
The current implementation focuses on a simplified version of the concept, utilizing a direction-based sequence instead of coordinates:

1. **Registration**:
    - The user inputs a seed to generate a sequence of directional movements (up, down, left, right, or stay).
    - The generated sequence is sent to the server and stored along with the user ID (coordinates are not sent).

2. **Login**:
    - The user inputs the seed again to regenerate the same sequence of movements.
    - The server generates a set of random challenges (e.g., 30 random steps) based on the stored sequence.
    - The client responds with the steps corresponding to the server's challenge, and the server verifies the response for authentication.

## Flexibility in Step Count
- The default setup uses a 1024-step sequence, which provides a high level of security, but the step count can be adjusted to balance between security and performance.
- This flexibility allows the system to adapt to different security needs and environments, potentially increasing the sequence to 2048 steps for enhanced protection.

## Future Directions
- The current prototype focuses on a direction-based sequence, but future iterations may explore full **coordinate-based random walk authentication**.
- Enhancing the challenge-response mechanism to further strengthen the system's security.
- Potential integration with hardware tokens for storing seeds securely and providing more robust authentication.

## Current Limitations and Notes
- The current implementation is not a full zero-knowledge proof system. It is a proof-of-concept focused on exploring the potential of random walks for authentication.
- The server only stores directional sequences, not the coordinates, minimizing the risk of sensitive data leakage.
- This project is still in the experimental phase and is open to feedback and contributions for further development.

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, JavaScript, CSS
- **Database**: SQLite (for demonstration purposes)

## Getting Started
This project is an experimental proof of concept. Please note that it is not yet production-ready. We welcome suggestions, feedback, and contributions to explore the potential of this authentication approach.

## Conclusion
RandomWalk-Auth represents an innovative approach to authentication, exploring the use of random walks for secure user verification. While still in its early stages, the project offers a unique perspective on non-traditional authentication methods.


# RandomWalk-Auth

## 概要
**RandomWalk-Auth** は、ランダムウォークを活用した認証方式の可能性を探るためのプロジェクトです。本プロジェクトは、従来のパスワードベースの方法に依存しない、柔軟でセキュアな認証アプローチを提供することを目指しています。ユーザーが提供するシードを基に、動作のシーケンスを生成し、安全な認証を実現することを目指しています。

## 理論的背景
**RandomWalk-Auth** のコンセプトは、ユーザーが提供するシードを基にした **ランダムウォーク** を利用して認証を行うことです。この方法は、サーバーに機密情報を保存することなく、チャレンジレスポンス形式の認証を行うことを目的としています。

1. **シードを用いたランダムウォークの生成**:
    - クライアント側でシードを基に初期座標 `(x0, y0)` を生成し、サーバーには共有されません。
    - この初期座標から、上下左右または動かないの5種類の動作で、指定されたステップ数のランダムウォーク（座標のリスト）を生成します。ステップ数はセキュリティ要件に応じて調整可能です。

2. **チャレンジレスポンス認証**:
    - クライアント側では、シードから生成した座標シーケンスを保持し、サーバー側には動作のシーケンスのみを送信します。
    - 認証プロセスでは、サーバーがランダムなチャレンジ（例：「n 番目と n+1 番目の方向は何ですか？」）を発行し、ユーザーが再生成されたシーケンスから回答します。
    - サーバーはユーザーの回答を検証し、認証を行います。

## 現在のプロトタイプの実装
現在のプロトタイプでは、以下のようにシンプルな方向シーケンスを用いた認証を行っています：

1. **登録**:
    - ユーザーがシードを入力し、上下左右（および動かない）の方向シーケンスを生成します。
    - 生成されたシーケンスはサーバーに送信され、ユーザーIDと共に保存されます（座標情報は送信されません）。

2. **ログイン**:
    - ユーザーが再度シードを入力し、同じ方向シーケンスを再生成します。
    - サーバーは保存されたシーケンスに基づいて、30個のランダムなステップを選び出しチャレンジを生成します。
    - クライアントは対応するステップを返し、サーバーがそれを検証して認証します。

## ステップ数の柔軟性
- デフォルトでは1024ステップを使用していますが、セキュリティレベルやパフォーマンスに応じて調整可能です。
- この柔軟性により、システムは異なるセキュリティ要件に対応し、2048ステップに増やすことでさらに高いセキュリティを確保することも可能です。

## 今後の方向性
- 今後の開発では、フル **座標ベースのランダムウォーク認証** への拡張を検討しています。
- より高度なチャレンジレスポンス方式を導入し、システムのセキュリティを強化します。
- ハードウェアトークンなどと連携し、シードを安全に保存することで、より堅牢な認証を提供する可能性があります。

## 現在の制約と注意点
- 現段階ではゼロ知識証明の完全な実装には至っていません。本プロジェクトはあくまで概念実証の段階です。
- サーバー側は動作シーケンスのみを保持し、座標情報は保持していないため、機密情報の漏洩リスクは最小限です。

## 技術スタック
- **バックエンド**: Python (Flask)
- **フロントエンド**: HTML, JavaScript, CSS
- **データベース**: SQLite（デモ用）

## おわりに
**RandomWalk-Auth** は、ランダムウォークを活用したユニークな認証方法の可能性を探るプロジェクトです。現段階では実験的な実装に留まっていますが、さらなる改良により、将来的にはより安全で柔軟な認証方式の構築が可能と考えています。