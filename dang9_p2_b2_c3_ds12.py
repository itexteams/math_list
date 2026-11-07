import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang9_p2_b2_c3_ds12(self):
                    # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
                    val_f1 = randint(-2, 2)            # f(1) - cực đại
                    val_f2 = val_f1 - randint(1, 3)    # f(2) - cực tiểu (phải nhỏ hơn f(1))
                    const_c = randint(2, 5)            # Hằng số c
                    val_sum_int = randint(4, 8)        # Tổng tích phân trị tuyệt đối từ 1 đến 4
                    
                    # Tính f(4) đúng: S = [f(1)-f(2)] + [f(4)-f(2)] => f(4) = S - f(1) + 2*f(2)
                    val_f4_dung = val_sum_int - val_f1 + 2 * val_f2
                    val_f4_sai = val_f4_dung + random.choice([-1, 1, 2])
                    
                    # Nội dung câu hỏi
                    noidungcauhoi = (r"""Cho hàm số $y=f(x)$ có bảng biến thiên như sau:
    \begin{center}
    \begin{tikzpicture}
    \tkzTabInit[espcl=1.5,lgt=1.2]{$x$/0.8,$f'(x)$/0.8,$f(x)$/2}
    {$-\infty$,$1$,$2$,$4$,$+\infty$}
    \tkzTabLine{,$+$,$0$,$-$,$0$,$+$,$0$,$-$,}
    \tkzTabVar{-/$-\infty$,+/$%s$,-/$%s$,+/$f(4)$,-/$-\infty$}
    \end{tikzpicture}
    \end{center}""" % (latex(val_f1), latex(val_f2)))

                    ########################################################################
                    # Nhận biết ############################################################
                    nb_da_1_d = r'\True Ta có $\int_{1}^{2} f^{\prime}(x) \text{d}x = %s$' % (latex(val_f2 - val_f1))
                    nb_da_1_s = r'Ta có $\int_{1}^{2} f^{\prime}(x) \text{d}x = %s$' % (latex(val_f1 - val_f2))
                    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                    nb_da_1 = random.choice(list_nb_da_1)
                    list_nb_1 = [nb_da_1]

                    loigiai_nb_1 = (r'Ta có $\int_{1}^{2} f^{\prime}(x) \text{d}x = f(2) - f(1) = %s - (%s) = %s$.' 
                                    % (latex(val_f2), latex(val_f1), latex(val_f2 - val_f1)))
                    list_nb_2 = [loigiai_nb_1]

                    # Xáo trộn Nhận biết
                    combined_nb = list(zip(list_nb_1, list_nb_2))
                    random.shuffle(combined_nb)
                    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                    ########################################################################
                    # Thông hiểu ###########################################################
                    val_const_part = 3 * const_c - val_f1
                    th_da_1_d = r'\True $\int_{1}^{4} [%s + f^{\prime}(x)] \text{d}x = f(4) + %s$' % (latex(const_c), latex(val_const_part))
                    th_da_1_s = r'$\int_{1}^{4} [%s + f^{\prime}(x)] \text{d}x = f(4) - %s$' % (latex(const_c), latex(val_const_part))
                    list_th_da_1 = [th_da_1_d, th_da_1_s]
                    th_da_1 = random.choice(list_th_da_1)
                    list_th_1 = [th_da_1]

                    loigiai_th_1 = (r'Ta có $\int_{1}^{4} [%s + f^{\prime}(x)] \text{d}x = %s x \Big|_1^4 + f(x) \Big|_1^4 = %s(4-1) + f(4) - f(1) = f(4) + %s$.' 
                                    % (latex(const_c), latex(const_c), latex(const_c), latex(val_const_part)))
                    list_th_2 = [loigiai_th_1]

                    # Xáo trộn Thông hiểu
                    combined_th = list(zip(list_th_1, list_th_2))
                    random.shuffle(combined_th)
                    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                    ########################################################################
                    # Vận dụng #############################################################
                    vd_da_1_d = r'\True $\int_{1}^{2} |f^{\prime}(x)| \text{d}x = f(1) - f(2)$'
                    vd_da_1_s = r'$\int_{1}^{2} |f^{\prime}(x)| \text{d}x = f(2) - f(1)$'
                    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                    vd_da_1 = random.choice(list_vd_da_1)
                    list_vd_1 = [vd_da_1]

                    loigiai_vd_1 = (r'''Trên đoạn $[1;2]$, dựa vào bảng biến thiên ta thấy $f'(x) \le 0$ nên $|f'(x)| = -f'(x)$. Vậy $\int_{1}^{2} |f^{\prime}(x)| \text{d}x = -\int_{1}^{2} f^{\prime}(x) \text{d}x = f(1) - f(2)$.''')
                    list_vd_2 = [loigiai_vd_1]

                    # Xáo trộn Vận dụng
                    combined_vd = list(zip(list_vd_1, list_vd_2))
                    random.shuffle(combined_vd)
                    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                    ########################################################################
                    # Vận dụng cao #########################################################
                    vdc_da_1_d = r'\True Nếu $\int_{1}^{4} |f^{\prime}(x)| \text{d}x = %s$ thì $f(4) = %s$' % (latex(val_sum_int), latex(val_f4_dung))
                    vdc_da_1_s = r'Nếu $\int_{1}^{4} |f^{\prime}(x)| \text{d}x = %s$ thì $f(4) = %s$' % (latex(val_sum_int), latex(val_f4_sai))
                    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                    vdc_da_1 = random.choice(list_vdc_da_1)
                    list_vdc_1 = [vdc_da_1]

                    loigiai_vdc_1 = (r'''Từ bảng biến thiên ta có: \\
    $%s = \int_{1}^{4} |f^{\prime}(x)| \text{d}x = \int_{1}^{2} |f^{\prime}(x)| \text{d}x + \int_{2}^{4} |f^{\prime}(x)| \text{d}x$\\
    $\Leftrightarrow %s = -\int_{1}^{2} f^{\prime}(x) \text{d}x + \int_{2}^{4} f^{\prime}(x) \text{d}x$\\
    $\Leftrightarrow %s = -[f(2)-f(1)] + [f(4)-f(2)] = f(1) - 2f(2) + f(4)$\\
    $\Leftrightarrow %s = %s - 2(%s) + f(4) \Leftrightarrow f(4) = %s$.''' 
                                    % (latex(val_sum_int), latex(val_sum_int), latex(val_sum_int), latex(val_sum_int), latex(val_f1), latex(val_f2), latex(val_f4_dung)))
                    list_vdc_2 = [loigiai_vdc_1]

                    # Xáo trộn Vận dụng cao
                    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                    random.shuffle(combined_vdc)
                    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

                    # --- KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (1-3) ---
                    def count_true_answers(answers):
                        return sum('\\True' in ans for ans in answers)

                    while True:
                        nb_sel = random.choice(list_nb_da_1)
                        th_sel = random.choice(list_th_da_1)
                        vd_sel = random.choice(list_vd_da_1)
                        vdc_sel = random.choice(list_vdc_da_1)
                        if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                            # Cập nhật lại list sau khi chọn thành công
                            shuffled_answers_nb = [nb_sel]
                            shuffled_answers_th = [th_sel]
                            shuffled_answers_vd = [vd_sel]
                            shuffled_answers_vdc = [vdc_sel]
                            break

                    # --- XUẤT NỘI DUNG ---
                    content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                        '\\choiceTFn \n'
                        '{' + str(shuffled_answers_nb[0]) + '}\n'
                        '{' + str(shuffled_answers_th[0]) + '}\n'
                        '{' + str(shuffled_answers_vd[0]) + '}\n'
                        '{' + str(shuffled_answers_vdc[0]) + '}\n'
                        '\\loigiai{ \n'
                        '\\begin{enumEX}[a)]{1} \n'
                        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                        '\\end{enumEX}} \n'
                        '\\end{ex}\n \\end{minipage} \n\n')
                    
                    return content