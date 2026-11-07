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


def bt_dang7_p2_b2_c2_hh12(self):
        # Khai báo biến
        x, y, z, t, k = symbols('x y z t k')
        
        while True:
            # VTCP và điểm đi qua của d1
            a1_d1 = random.choice([1, -1, 2, -2, 3, -3])
            b1_d1 = random.choice([1, -1, 2, -2, 3, -3])
            c1_d1 = random.choice([1, -1, 2, -2, 3, -3])
            x0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])
            y0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])
            z0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])
            
            # VTCP và điểm đi qua của d2
            a2_d2 = random.choice([1, -1, 2, -2, 3, -3])
            b2_d2 = random.choice([1, -1, 2, -2, 3, -3])
            c2_d2 = random.choice([1, -1, 2, -2, 3, -3])
            x0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])
            y0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])
            z0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])

            # Chọn tham số t1 cho A thuộc d1, t2 cho B thuộc d2
            t1 = 1
            t2 = -1

            A_x = x0_d1 + a1_d1 * t1
            A_y = y0_d1 + b1_d1 * t1
            A_z = z0_d1 + c1_d1 * t1

            B_x = x0_d2 + a2_d2 * t2
            B_y = y0_d2 + b2_d2 * t2
            B_z = z0_d2 + c2_d2 * t2

            # Đảm bảo A và B không trùng nhau
            if (A_x, A_y, A_z) == (B_x, B_y, B_z):
                continue

            # Đảm bảo d1 và d2 không cùng phương
            u1 = Matrix([a1_d1, b1_d1, c1_d1])
            u2 = Matrix([a2_d2, b2_d2, c2_d2])
            cross_u = [b1_d1 * c2_d2 - c1_d1 * b2_d2,
                       c1_d1 * a2_d2 - a1_d1 * c2_d2,
                       a1_d1 * b2_d2 - b1_d1 * a2_d2]
            if cross_u == [0, 0, 0]:
                continue

            # Để A, M, B thẳng hàng: chọn M là trung điểm AB (hoặc M chia đoạn AB)
            # Chọn M nguyên: kiểm tra tính chẵn lẻ để M có tọa độ nguyên đẹp
            if (A_x + B_x) % 2 == 0 and (A_y + B_y) % 2 == 0 and (A_z + B_z) % 2 == 0:
                Mx = (A_x + B_x) // 2
                My = (A_y + B_y) // 2
                Mz = (A_z + B_z) // 2
                # Tránh trường hợp M trùng A hoặc B
                if (Mx, My, Mz) != (A_x, A_y, A_z):
                    break

        # Nội dung câu hỏi (chú ý sửa \frac{y+%s}{%s} thành \frac{y-%s}{%s})
        noidungcauhoi = ('''Trong không gian $Oxyz$, cho điểm $M(%s;%s;%s)$ và hai đường thẳng 
\\begin{center} 
$d_1: \\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$, \\quad $d_2: \\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$. 
\\end{center} 
Đường thẳng $d$ qua $M$ cắt $d_1$, $d_2$ lần lượt tại $A$ và $B$.'''
                         % (latex(Mx), latex(My), latex(Mz),
                            latex(x0_d1), latex(a1_d1), latex(y0_d1), latex(b1_d1), latex(z0_d1), latex(c1_d1),
                            latex(x0_d2), latex(a2_d2), latex(y0_d2), latex(b2_d2), latex(z0_d2), latex(c2_d2)))
        
        ################################ Nhận biết ################################
        # Các đáp án
        nb_da_1_d = '\\True $A(%s;%s;%s)$ và $B(%s;%s;%s)$' % (latex(A_x), latex(A_y), latex(A_z), latex(B_x), latex(B_y), latex(B_z))
        nb_da_1_s = '$A(%s;%s;%s)$ và $B(%s;%s;%s)$' % (latex(A_x + 1), latex(A_y), latex(A_z), latex(B_x), latex(B_y), latex(B_z))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Điểm $A \\in d_1 \\Rightarrow A(%s + %s t;\\, %s + %s t;\\, %s + %s t)$. \\\\
Điểm $B \\in d_2 \\Rightarrow B(%s + %s t';\\, %s + %s t';\\, %s + %s t')$. \\\\
Ba điểm $A, M, B$ thẳng hàng khi và chỉ khi tồn tại số thực $k$ sao cho $\\vec{AM} = k\\vec{MB}$ (hoặc $\\vec{AM}$ cùng phương $\\vec{AB}$). Giải hệ điều kiện ta được $t = %s$ và $t' = %s$, suy ra $A(%s;%s;%s)$ và $B(%s;%s;%s)$.'''
            % (latex(x0_d1), latex(a1_d1), latex(y0_d1), latex(b1_d1), latex(z0_d1), latex(c1_d1),
               latex(x0_d2), latex(a2_d2), latex(y0_d2), latex(b2_d2), latex(z0_d2), latex(c2_d2),
               latex(t1), latex(t2),
               latex(A_x), latex(A_y), latex(A_z), latex(B_x), latex(B_y), latex(B_z)))
        
        list_nb_2 = [loigiai_nb_1]
        combined_nb = list(zip(list_nb_1, list_nb_2))
        random.shuffle(combined_nb)
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        ################################ Thông hiểu ################################
        vec_AM = [Mx - A_x, My - A_y, Mz - A_z]
        vec_BM = [Mx - B_x, My - B_y, Mz - B_z]
        AM_mag = sqrt(vec_AM[0]**2 + vec_AM[1]**2 + vec_AM[2]**2)
        BM_mag = sqrt(vec_BM[0]**2 + vec_BM[1]**2 + vec_BM[2]**2)
        ratio = Rational(AM_mag, BM_mag)
        
        th_da_1_d = '\\True $|\\vec{AM}| = %s|\\vec{BM}|$' % latex(ratio)
        th_da_1_s = '$|\\vec{AM}| = %s|\\vec{BM}|$' % latex(ratio + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        list_th_1 = [th_da_1]
        
        loigiai_th_1 = ('''Từ tọa độ các điểm $A, B, M$ ta tính được: \\\\
$AM = \\sqrt{(%s)^2+(%s)^2+(%s)^2} = %s$. \\\\
$BM = \\sqrt{(%s)^2+(%s)^2+(%s)^2} = %s$. \\\\
Do đó $|\\vec{AM}| = %s|\\vec{BM}|$.'''
            % (latex(vec_AM[0]), latex(vec_AM[1]), latex(vec_AM[2]), latex(AM_mag),
               latex(vec_BM[0]), latex(vec_BM[1]), latex(vec_BM[2]), latex(BM_mag),
               latex(ratio)))
        
        list_th_2 = [loigiai_th_1]
        combined_th = list(zip(list_th_1, list_th_2))
        random.shuffle(combined_th)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        ################################ Vận dụng ################################
        OB_mag = sqrt(B_x**2 + B_y**2 + B_z**2)
        
        vd_da_1_d = '\\True Khoảng cách từ gốc tọa độ $O$ đến điểm $B$ là $OB = %s$' % latex(OB_mag)
        vd_da_1_s = 'Khoảng cách từ gốc tọa độ $O$ đến điểm $B$ là $OB = %s$' % latex(OB_mag + 1)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        list_vd_1 = [vd_da_1]
        
        loigiai_vd_1 = ('''Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $B(%s;%s;%s)$ là: \\\\
$OB = \\sqrt{(%s)^2+(%s)^2+(%s)^2} = %s$.'''
            % (latex(B_x), latex(B_y), latex(B_z),
               latex(B_x), latex(B_y), latex(B_z),
               latex(OB_mag)))
        
        list_vd_2 = [loigiai_vd_1]
        combined_vd = list(zip(list_vd_1, list_vd_2))
        random.shuffle(combined_vd)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        ################################ Vận dụng cao ################################
        vec_BA = [A_x - B_x, A_y - B_y, A_z - B_z]
        
        vdc_da_1_d = ('\\True Đường thẳng $d$ đi qua $A(%s;%s;%s)$ và có vectơ chỉ phương $\\vec{u} = (%s;%s;%s)$ có phương trình chính tắc là '
                      '$\\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$') % (
            latex(A_x), latex(A_y), latex(A_z),
            latex(vec_BA[0]), latex(vec_BA[1]), latex(vec_BA[2]),
            latex(A_x), latex(vec_BA[0]), latex(A_y), latex(vec_BA[1]), latex(A_z), latex(vec_BA[2])
        )
        vdc_da_1_s = ('Đường thẳng $d$ đi qua $A(%s;%s;%s)$ và có vectơ chỉ phương $\\vec{u} = (%s;%s;%s)$ có phương trình chính tắc là '
                      '$\\frac{x+%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$') % (
            latex(A_x), latex(A_y), latex(A_z),
            latex(vec_BA[0]), latex(vec_BA[1]), latex(vec_BA[2]),
            latex(A_x + 1), latex(vec_BA[0]), latex(A_y), latex(vec_BA[1]), latex(A_z), latex(vec_BA[2])
        )
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        list_vdc_1 = [vdc_da_1]
        
        loigiai_vdc_1 = ('''Đường thẳng $d$ đi qua $A(%s;%s;%s)$ và nhận $\\vec{BA} = (%s;%s;%s)$ làm một vectơ chỉ phương. \\\\
Phương trình chính tắc của $d$ là: $\\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$.'''
            % (latex(A_x), latex(A_y), latex(A_z),
               latex(vec_BA[0]), latex(vec_BA[1]), latex(vec_BA[2]),
               latex(A_x), latex(vec_BA[0]), latex(A_y), latex(vec_BA[1]), latex(A_z), latex(vec_BA[2])))
        
        list_vdc_2 = [loigiai_vdc_1]
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        random.shuffle(combined_vdc)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
        
        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)
        
        # Lặp đến khi có từ 1 đến 3 đáp án đúng
        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break
        
        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]
        
        combined_nb = list(zip(list_nb_1, list_nb_2))
        combined_th = list(zip(list_th_1, list_th_2))
        combined_vd = list(zip(list_vd_1, list_vd_2))
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
        
        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n'
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
                   '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+')
        return content
