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


def bt_dang16_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên
            k = random.choice([10, 12, 14])
            mul_C = random.choice([10, 20])
            mul_I = random.choice([10, 20])
            mul_V = random.choice([10, 20])

            C_X = mul_C
            I_X = 2 * mul_I
            V_X = mul_V

            C_Y = mul_C
            I_Y = mul_I
            V_Y = 2 * mul_V

            Req_C = mul_C * k
            Req_I = mul_I * (k + 4)
            Req_V = mul_V * (k + 2)

            p_1 = random.choice([15000, 20000, 30000])
            p_2 = p_1 + random.choice([2000, 5000, 8000])

            pt_min_x = k - 2
            pt_min_y = 2
            pt_false_x = 4
            pt_false_y = k - 4

            pt_test_x = k - 2
            pt_test_y = k - 2

            desc_str = "mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Hoà cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bà Hoà được tư vấn bổ sung chế độ ăn kiêng đặc biệt bằng cách sử dụng hai loại thực phẩm khác nhau là $X$ và $Y$. Mỗi gói thực phẩm $X$ chứa %s đơn vị canxi, %s đơn vị sắt và %s đơn vị vitamin $B$. Mỗi gói thực phẩm $Y$ chứa %s đơn vị canxi, %s đơn vị sắt và %s đơn vị vitamin $B$. Yêu cầu hằng ngày tối thiểu trong chế độ ăn uống là %s đơn vị canxi, %s đơn vị sắt và %s đơn vị vitamin $B$. Mỗi ngày không được dùng quá %s gói mỗi loại.'''              
                             % (C_X, I_X, V_X, C_Y, I_Y, V_Y, Req_C, Req_I, Req_V, k))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hệ bất phương trình %s là $\\begin{cases} x + y \\ge %s \\\\ 2x + y \\ge %s \\\\ x + 2y \\ge %s \\\\ 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\end{cases}$.' % (desc_str, k, k+4, k+2, k, k)
            nb_da_1_s = 'Hệ bất phương trình %s là $\\begin{cases} x + y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 2y \\ge %s \\\\ 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\end{cases}$.' % (desc_str, k, k+4, k+2, k, k)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $x$, $y$ lần lượt là số gói thực phẩm loại $X$ và loại $Y$ mà bà Hoà sử dụng mỗi ngày. \\\\
            Điều kiện: $0 \\le x \\le %s$ và $0 \\le y \\le %s$. \\\\
            Tổng lượng canxi là: $%s x + %s y$. Do yêu cầu tối thiểu %s đơn vị canxi nên ta có: $%s x + %s y \\ge %s \\Leftrightarrow x + y \\ge %s$. \\\\
            Tổng lượng sắt là: $%s x + %s y$. Do yêu cầu tối thiểu %s đơn vị sắt nên ta có: $%s x + %s y \\ge %s \\Leftrightarrow 2x + y \\ge %s$. \\\\
            Tổng lượng vitamin B là: $%s x + %s y$. Do yêu cầu tối thiểu %s đơn vị vitamin B nên ta có: $%s x + %s y \\ge %s \\Leftrightarrow x + 2y \\ge %s$. \\\\
            Vậy ta có hệ bất phương trình thỏa mãn điều kiện bài toán là: $\\begin{cases} x + y \\ge %s \\\\ 2x + y \\ge %s \\\\ x + 2y \\ge %s \\\\ 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\end{cases}$.'''
                       % (k, k, C_X, C_Y, Req_C, C_X, C_Y, Req_C, k, I_X, I_Y, Req_I, I_X, I_Y, Req_I, k+4, V_X, V_Y, Req_V, V_X, V_Y, Req_V, k+2, k, k+4, k+2, k, k))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình %s là một ngũ giác.' % (desc_str)
            th_da_1_s = 'Miền nghiệm của hệ bất phương trình %s là một tứ giác.' % (desc_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            clip_max = k + 3
            y1_start = k + 8
            y1_end = k + 4 - 2 * clip_max
            y2_start = k + 2
            y2_end = k - clip_max
            y3_start = (k + 4) / 2.0
            y3_end = (k + 2 - clip_max) / 2.0

            # Nội dung lời giải
            loigiai_th_1 = ('''Vẽ các đường thẳng $d_1: x + y = %s$, $d_2: 2x + y = %s$, $d_3: x + 2y = %s$, $x = %s$, $y = %s$ trên cùng một mặt phẳng tọa độ $Oxy$. \\\\
            Miền nghiệm của hệ bất phương trình là phần mặt phẳng không bị gạch chéo trong hình vẽ dưới đây (bao gồm cả bờ). \\\\
            Quan sát hình vẽ, ta thấy miền nghiệm là ngũ giác có các đỉnh tương ứng là $A(2; %s)$, $B(4; %s)$, $C(%s; 2)$, $D(%s; 1)$ và $E(%s; %s)$. \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.3, line width=1pt]
            \\draw[->] (-2, 0) -- (%s, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, %s) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (%s,%s);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (%s,%s);
            \\fill[white] (2, %s) -- (4, %s) -- (%s, 2) -- (%s, 1) -- (%s, %s) -- cycle;
            \\draw[->] (-2, 0) -- (%s, 0);
            \\draw[->] (0, -2) -- (0, %s);
            \\draw[black] (-2, %s) -- (%s, %s); 
            \\draw[black] (-2, %s) -- (%s, %s); 
            \\draw[black] (-2, %s) -- (%s, %s); 
            \\draw[black] (%s, -2) -- (%s, %s); 
            \\draw[black] (-2, %s) -- (%s, %s); 
            \\coordinate (V1) at (2, %s);
            \\coordinate (V2) at (4, %s);
            \\coordinate (V3) at (%s, 2);
            \\coordinate (V4) at (%s, 1);
            \\coordinate (V5) at (%s, %s);
            \\fill (V1) circle (5pt);
            \\fill (V2) circle (5pt);
            \\fill (V3) circle (5pt);
            \\fill (V4) circle (5pt);
            \\fill (V5) circle (5pt);
            \\end{tikzpicture}
            \\end{center}'''       
                       % (k, k+4, k+2, k, k, k, k-4, k-2, k, k, k,
                          clip_max, clip_max, clip_max, clip_max, clip_max, clip_max,
                          k, k-4, k-2, k, k, k,
                          clip_max, clip_max,
                          y1_start, clip_max, y1_end,
                          y2_start, clip_max, y2_end,
                          y3_start, clip_max, y3_end,
                          k, k, clip_max,
                          k, clip_max, k,
                          k, k-4, k-2, k, k, k))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Biết $1$ gói thực phẩm loại $X$ giá $%s$ đồng, $1$ gói thực phẩm loại $Y$ giá $%s$ đồng. Bà Hoà cần dùng $%s$ gói thực phẩm loại $X$ và $%s$ gói thực phẩm loại $Y$ để chi phí mua là ít nhất.' % (p_1, p_2, pt_min_x, pt_min_y)
            vd_da_1_s = 'Biết $1$ gói thực phẩm loại $X$ giá $%s$ đồng, $1$ gói thực phẩm loại $Y$ giá $%s$ đồng. Bà Hoà cần dùng $%s$ gói thực phẩm loại $X$ và $%s$ gói thực phẩm loại $Y$ để chi phí mua là ít nhất.' % (p_1, p_2, pt_false_x, pt_false_y)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            F1 = p_1 * 2 + p_2 * k
            F2 = p_1 * 4 + p_2 * (k - 4)
            F3 = p_1 * (k - 2) + p_2 * 2
            F4 = p_1 * k + p_2 * 1
            F5 = p_1 * k + p_2 * k
            min_F = min(F1, F2, F3, F4, F5)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $F(x; y)$ là tổng chi phí để mua thức ăn mỗi ngày. Ta có $F(x; y) = %s x + %s y$. \\\\
            Tính giá trị của biểu thức $F(x; y)$ tại các đỉnh của miền nghiệm ngũ giác, ta được: \\\\
            Tọa độ đỉnh $A(2; %s) \\Rightarrow F(2; %s) = %s \\cdot 2 + %s \\cdot %s = %s$. \\\\
            Tọa độ đỉnh $B(4; %s) \\Rightarrow F(4; %s) = %s \\cdot 4 + %s \\cdot %s = %s$. \\\\
            Tọa độ đỉnh $C(%s; 2) \\Rightarrow F(%s; 2) = %s \\cdot %s + %s \\cdot 2 = %s$. \\\\
            Tọa độ đỉnh $D(%s; 1) \\Rightarrow F(%s; 1) = %s \\cdot %s + %s \\cdot 1 = %s$. \\\\
            Tọa độ đỉnh $E(%s; %s) \\Rightarrow F(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Giá trị nhỏ nhất của $F(x; y)$ là $%s$, đạt được khi $x = %s$ và $y = %s$. \\\\
            Vậy bà Hoà cần dùng $%s$ gói thực phẩm loại $X$ và $%s$ gói thực phẩm loại $Y$ để chi phí mua là ít nhất.''' 
                       % (p_1, p_2, k, k, p_1, p_2, k, F1, k-4, k-4, p_1, p_2, k-4, F2, k-2, k-2, p_1, k-2, p_2, F3, k, k, p_1, k, p_2, F4, k, k, k, k, p_1, k, p_2, k, F5, min_F, pt_min_x, pt_min_y, pt_min_x, pt_min_y))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Điểm $(%s; %s)$ thuộc miền nghiệm của hệ bất phương trình %s.' % (pt_test_x, pt_test_y, desc_str)
            vdc_da_1_s = 'Điểm $(%s; %s)$ không thuộc miền nghiệm của hệ bất phương trình %s.' % (pt_test_x, pt_test_y, desc_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Thay $x = %s$ và $y = %s$ vào hệ bất phương trình ta được: \\\\
            $\\begin{cases} %s + %s \\ge %s \\\\ 2 \\cdot %s + %s \\ge %s \\\\ %s + 2 \\cdot %s \\ge %s \\\\ 0 \\le %s \\le %s \\\\ 0 \\le %s \\le %s \\end{cases}$. \\\\
            Tất cả các bất đẳng thức trên đều đúng. Vậy điểm $(%s; %s)$ có thuộc miền nghiệm của hệ bất phương trình.'''
                       % (pt_test_x, pt_test_y, pt_test_x, pt_test_y, k, pt_test_x, pt_test_y, k+4, pt_test_x, pt_test_y, k+2, pt_test_x, k, pt_test_y, k, pt_test_x, pt_test_y))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

