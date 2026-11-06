import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang40_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            x = symbols('x')

            # Random các điểm giao cắt của đồ thị với trục hoành, đảm bảo S1 > S2
            x1 = random.randint(5, 8)
            x2 = random.randint(x1 + 2, x1 + 4)
            x3 = random.randint(x2 + 3, x2 + 5)

            # BƯỚC ĐỘT PHÁ: Dùng Python định nghĩa một hàm đa thức đi qua đúng 4 nghiệm (0, x1, x2, x3)
            # Hàm có dạng: y = k * x * (x - x1) * (x - x2) * (x3 - x)
            # Tính hệ số k sao cho chiều cao của đỉnh S1 rơi vào khoảng 4.0 để đồ thị cân đối
            x_mid = x1 / 2.0
            y_raw = x_mid * (x_mid - x1) * (x_mid - x2) * (x3 - x_mid)
            k = 4.0 / abs(y_raw)

            def get_y(xv):
                return k * xv * (xv - x1) * (xv - x2) * (x3 - xv)

            # Hàm sinh tọa độ nối tiếp nhau (tạo độ mịn tuyệt đối)
            def gen_path(x_start, x_end, n_samples=40):
                step = (x_end - x_start) / n_samples
                pts = []
                for i in range(n_samples + 1):
                    xv = x_start + i * step
                    yv = get_y(xv)
                    pts.append("(%.3f,%.3f)" % (xv, yv))
                return " -- ".join(pts)

            # Sinh các đường dẫn để tô màu và vẽ viền
            path_S1 = gen_path(0, x1, 40)
            path_S2 = gen_path(x1, x2, 30)
            path_S3 = gen_path(x2, x3, 30)
            path_full = gen_path(-0.8, x3 + 0.8, 80)

            # Nội dung hình vẽ TikZ đã được thay thế bằng tọa độ toán học siêu mịn
            tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.6, thick]
            \\fill[green!10] %s -- cycle;
            \\fill[green!10] %s -- cycle;
            \\fill[green!10] %s -- cycle;
            \\draw[blue, thick] %s;
            \\node at (%.2f, %.2f) {$S_1$};
            \\node at (%.2f, %.2f) {$S_2$};
            \\node at (%.2f, %.2f) {$S_3$};
            \\node[below left] at (%s, 0) {$%s$};
            \\node[above left] at (%s, 0) {$%s$};
            \\node[above right] at (%s, 0) {$%s$};
            \\draw[->] (-1.5,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,-4.5) -- (0,5.5) node[right] {$y$};
            \\node at (-0.3, -0.3) {$O$};
            \\end{tikzpicture}
            \\end{center}''' % (
                path_S1, path_S2, path_S3, path_full,
                x1 * 0.5, get_y(x1 * 0.5) * 0.4,
                (x1 + x2) * 0.5, get_y((x1 + x2) * 0.5) * 0.4,
                (x2 + x3) * 0.5, get_y((x2 + x3) * 0.5) * 0.4,
                x1, x1,
                x2, x2,
                x3, x3,
                x3 + 1.5
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=g(x)$ có đồ thị như hình vẽ và đặt $f(x)=\\int\\limits_0^x g(t)\\mathrm{d}t$. Gọi $S_1, S_2$ và $S_3$ lần lượt là diện tích của các phần hình phẳng được tô màu.
            %s''' % (tikz_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $y=f(x)$ đạt cực đại tại điểm $x=%s$' % (x1)
            nb_da_1_s = 'Hàm số $y=f(x)$ đạt cực tiểu tại điểm $x=%s$' % (x1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Cấu trúc lời giải cơ bản (chưa bao gồm đánh giá đúng sai)
            base_loigiai_nb_1 = ('''Ta có $f(x)=\\int\\limits_0^x g(t)\\mathrm{d}t \\Rightarrow f'(x)=g(x)$. \\\\
            Tại $x=%s$ thì đạo hàm $f'(x)$ đổi dấu từ dương sang âm nên hàm số đạt cực đại tại $x=%s$''' % (x1, x1))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Giá trị của hàm số tại $x=%s$ là $f(%s)=S_1-S_2$' % (x2, x2)
            th_da_1_s = 'Giá trị của hàm số tại $x=%s$ là $f(%s)=S_1+S_2$' % (x2, x2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_th_1 = ('''Ta có $f(%s)=\\int\\limits_0^{%s} g(t)\\mathrm{d}t = \\int\\limits_0^{%s} g(t)\\mathrm{d}t + \\int\\limits_{%s}^{%s} g(t)\\mathrm{d}t = S_1 - S_2$''' % (x2, x2, x1, x1, x2))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hàm số $y=f(x)$ nghịch biến trên khoảng $(%s;%s)$' % (x1, x2)
            vd_da_1_s = 'Hàm số $y=f(x)$ đồng biến trên khoảng $(%s;%s)$' % (x1, x2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_vd_1 = ('''Trên khoảng $(%s;%s)$ thì đồ thị hàm số $y=g(x)$ nằm phía dưới trục hoành. \\\\
            Mặt khác: $g(x)=f'(x)<0, \\forall x \\in (%s;%s)$ suy ra hàm số nghịch biến''' % (x1, x2, x1, x2))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Phương trình $f(x)=0$ có đúng một nghiệm phân biệt trên $[0;%s]$' % (x3)
            vdc_da_1_s = 'Phương trình $f(x)=0$ có đúng hai nghiệm phân biệt trên $[0;%s]$' % (x3)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_vdc_1 = ('''Xét $f(0)=0$. \\\\
            Khi $x \\in (0;%s)$ thì $f(x)$ đồng biến và $f(%s)=S_1>0$. \\\\
            Khi $x \\in (%s;%s)$ thì $f(x)$ nghịch biến và $f(%s)=S_1-S_2$. \\\\
            Khi $x \\in (%s;%s)$ thì $f(x)$ đồng biến do $g(x)>0$ và từ đồ thị thì $S_1>S_2 \\Rightarrow S_1-S_2>0$. \\\\
            Vậy hàm số $f(x)$ chỉ cắt trục hoành tại điểm duy nhất là $x=0$''' % (x1, x1, x1, x2, x2, x2, x3))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Sinh lời giải với kết luận đúng/sai linh hoạt tương ứng vào mệnh đề vừa được chọn
            loigiai_nb_1 = base_loigiai_nb_1 + (' nên mệnh đề này đúng.' if '\\True' in nb_da_1 else ' nên mệnh đề này sai.')
            loigiai_th_1 = base_loigiai_th_1 + (' nên mệnh đề này đúng.' if '\\True' in th_da_1 else ' nên mệnh đề này sai.')
            loigiai_vd_1 = base_loigiai_vd_1 + (' nên mệnh đề này đúng.' if '\\True' in vd_da_1 else ' nên mệnh đề này sai.')
            loigiai_vdc_1 = base_loigiai_vdc_1 + (' nên mệnh đề này đúng.' if '\\True' in vdc_da_1 else ' nên mệnh đề này sai.')

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

