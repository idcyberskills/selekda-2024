<?php
require 'db.php';
session_start();

if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit();
}

$user_id = $_SESSION['user_id'];

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['note'])) {
    $note = filter_input(INPUT_POST, 'note', FILTER_SANITIZE_STRING);
    
    $stmt = $pdo->prepare('INSERT INTO notes (user_id, note) VALUES (:user_id, :note)');
    $stmt->execute(['user_id' => $user_id, 'note' => $note]);
}

if (isset($_GET['delete'])) {
    $note_id = filter_input(INPUT_GET, 'delete', FILTER_VALIDATE_INT);
    $stmt = $pdo->prepare('DELETE FROM notes WHERE id = :id AND user_id = :user_id');
    $stmt->execute(['id' => $note_id, 'user_id' => $user_id]);
}

$stmt = $pdo->prepare('SELECT * FROM notes WHERE user_id = :user_id ORDER BY created_at DESC');
$stmt->execute(['user_id' => $user_id]);
$notes = $stmt->fetchAll();
?>

<h2>Your Notes</h2>

<form method="post">
    <textarea name="note" required></textarea><br>
    <input type="submit" value="Add Note">
</form>

<ul>
    <?php foreach ($notes as $note): ?>
        <li>
            <?php echo $note['note']; ?>
            <a href="?delete=<?php echo $note['id']; ?>">Delete</a>
        </li>
    <?php endforeach; ?>
</ul>