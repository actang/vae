import matplotlib.pyplot as plt
import numpy as np
import os as os

def dataset_sample_plot(FLAGS, dataset, ncol=10):
    number_of_images_per_column = min(FLAGS.image_num_categories, ncol)
    random_sample_plot_idx = np.random.choice(
        range(dataset.train.num_examples),
        size=number_of_images_per_column * number_of_images_per_column
    )
    sample_canvas = np.zeros(
        (
            FLAGS.image_height * number_of_images_per_column,
            FLAGS.image_width * number_of_images_per_column,
            FLAGS.image_channel
        )
    )
    for row_idx in range(number_of_images_per_column):
        for column_idx in range(number_of_images_per_column):
            sample_canvas[
                row_idx * FLAGS.image_height:
                (row_idx + 1) * FLAGS.image_height,
                column_idx * FLAGS.image_width:
                (column_idx + 1) * FLAGS.image_width,
                :] = dataset.train.images[
                    random_sample_plot_idx[(row_idx + 1) * (column_idx + 1) - 1]
                ].reshape(
                    FLAGS.image_height,
                    FLAGS.image_width,
                    FLAGS.image_channel
                )
    plt.figure(figsize=(7, 7))
    plt.axis('off')
    if sample_canvas.shape[2] == 1:
        canvas = sample_canvas[:, :, 0]
        plt.imshow(canvas, cmap="gray")
    else:
        plt.imshow(sample_canvas)
    plt.title('Sample Images from {0}'.format(FLAGS.dataset_name))
    plt.savefig(
        os.path.join(
            FLAGS.figures_path,
            "{}_sample_plots.png".format(FLAGS.dataset_name)
        )
    )
    plt.close()


def vae_plot_sampled(FLAGS, sampled_images, current_epoch, ncol=6):
    sampled_canvas = np.zeros(
        (
            FLAGS.image_height * ncol,
            FLAGS.image_width * ncol,
            FLAGS.image_channel
        )
    )
    for row_idx in range(ncol):
        for colume_idx in range(ncol):
            sampled_canvas[
                row_idx * FLAGS.image_height:
                (row_idx + 1) * FLAGS.image_height,
                colume_idx * FLAGS.image_width:
                (colume_idx + 1) * FLAGS.image_width,
                :] = sampled_images[
                    row_idx * ncol + colume_idx
                ].reshape(
                    FLAGS.image_height,
                    FLAGS.image_width,
                    FLAGS.image_channel
                )
    plt.figure(figsize=(7, 7))
    plt.axis('off')
    if sampled_canvas.shape[2] == 1:
        sampled_canvas = sampled_canvas[:, :, 0]
        plt.imshow(sampled_canvas, cmap="gray")
    else:
        plt.imshow(sampled_canvas)
    plt.title('VAE Sampled Images from {0}'.format(FLAGS.dataset_name))
    plt.savefig(
        os.path.join(
            FLAGS.figures_path,
            "{0}_VAE_{1}_sample_epoch_{2}.png".format(
                FLAGS.dataset_name,
                FLAGS.vae_name,
                current_epoch
            )
        )
    )
    plt.close()


def vae_plot_reconstructed(FLAGS, target_images, reconstructed_images,
                           current_epoch, ncol=6):
    reconstructed_canvas = np.zeros(
        (
            FLAGS.image_height * ncol,
            FLAGS.image_width * ncol,
            FLAGS.image_channel
        )
    )
    for row_idx in range(ncol):
        for column_idx in range(ncol):
            if column_idx % 2 == 0:
                reconstructed_canvas[
                    row_idx * FLAGS.image_height:
                    (row_idx + 1) * FLAGS.image_height,
                    column_idx * FLAGS.image_width:
                    (column_idx + 1) * FLAGS.image_width,
                    :] = target_images[
                        row_idx * ncol + column_idx
                    ].reshape(
                        FLAGS.image_height,
                        FLAGS.image_width,
                        FLAGS.image_channel
                    )
            else:
                reconstructed_canvas[
                    row_idx * FLAGS.image_height:
                    (row_idx + 1) * FLAGS.image_height,
                    column_idx * FLAGS.image_width:
                    (column_idx + 1) * FLAGS.image_width,
                    :] = reconstructed_images[
                        row_idx * ncol + column_idx - 1
                    ].reshape(
                        FLAGS.image_height,
                        FLAGS.image_width,
                        FLAGS.image_channel
                    )
    plt.figure(figsize=(7, 7))
    plt.axis('off')
    if reconstructed_canvas.shape[2] == 1:
        canvas = reconstructed_canvas[:, :, 0]
        plt.imshow(canvas, cmap="gray")
    else:
        plt.imshow(reconstructed_canvas)
    plt.title('VAE Reconstructed Images from {0} \n Raw images (left) '
              'v.s. Reconstructed images (right)'.format(FLAGS.dataset_name))
    plt.savefig(
        os.path.join(
            FLAGS.figures_path,
            "{0}_VAE_{1}_reconstructed_epoch_{2}.png".format(
                FLAGS.dataset_name,
                FLAGS.vae_name,
                current_epoch
            )
        )
    )
    plt.close()


def plot_all_images(FLAGS, sampled_images, current_iteration, theme, title,
                    ncol=6):
    sampled_canvas = np.zeros(
        (
            FLAGS.image_height * ncol,
            FLAGS.image_width * ncol,
            FLAGS.image_channel
        )
    )
    for row_idx in range(ncol):
        for colume_idx in range(ncol):
            sampled_canvas[
                row_idx * FLAGS.image_height:
                (row_idx + 1) * FLAGS.image_height,
                colume_idx * FLAGS.image_width:
                (colume_idx + 1) * FLAGS.image_width,
                :] = sampled_images[
                    row_idx * ncol + colume_idx
                ].reshape(
                    FLAGS.image_height,
                    FLAGS.image_width,
                    FLAGS.image_channel
                )
    plt.figure(figsize=(7, 7))
    plt.axis('off')
    if sampled_canvas.shape[2] == 1:
        sampled_canvas = sampled_canvas[:, :, 0]
        plt.imshow(sampled_canvas, cmap="gray")
    else:
        plt.imshow(sampled_canvas)
    plt.title('{0} Images from {1} at Iteration {2} ({3})'.format(
        theme,
        FLAGS.dataset_name,
        current_iteration,
        title
    ))
    plt.savefig(
        os.path.join(
            FLAGS.figures_path,
            "{0}_{1}_iteration_{2}_{3}.png".format(
                FLAGS.dataset_name,
                theme,
                current_iteration,
                title
            )
        )
    )
    plt.close()
