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


def bt_dang25_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Điểm đúng cho câu A
            true_points = [(3, 10), (5, 8), (9, 4), (11, 2)]
            tp = random.choice(true_points)

            # Điểm sai cho câu A (cố tình chọn điểm có tổng < 12 để dễ giải thích)
            false_points = [(2, 9), (4, 7), (8, 3), (10, 1)]
            fp = random.choice(false_points)

            # Tham số cho câu D (Random hệ số của biểu thức F = cx*x + cy*y)
            cx = random.choice([10, 15, 20, 25, 30])
            cy = random.choice([10, 15, 20, 25, 30])

            # Các đỉnh của đa giác miền nghiệm
            vertices = [(2, 12), (4, 8), (10, 2), (12, 1), (12, 12)]

            # Tính min của F(x,y)
            vals = [cx * vx + cy * vy for vx, vy in vertices]
            min_val = min(vals)
            false_min_val = min_val + random.choice([10, 15, 20, 30])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình: $\\begin{cases} x + y \\ge 12 \\\\ 2x + y \\ge 16 \\\\ x + 2y \\ge 14 \\\\ 0 \\le x \\le 12 \\\\ 0 \\le y \\le 12 \\end{cases} (I)$.''')

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $(%s; %s)$ là một nghiệm của hệ bất phương trình $(I)$' % (tp[0], tp[1])
            nb_da_1_s = '$(%s; %s)$ là một nghiệm của hệ bất phương trình $(I)$' % (fp[0], fp[1])
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1_d = ('''Thay $x=%s, y=%s$ vào hệ bất phương trình $(I)$ ta thấy: \\\\
            $\\begin{cases} %s + %s = %s \\ge 12 \\\\ 2 \\cdot %s + %s = %s \\ge 16 \\\\ %s + 2 \\cdot %s = %s \\ge 14 \\\\ 0 \\le %s \\le 12 \\\\ 0 \\le %s \\le 12 \\end{cases}$ (thỏa mãn). \\\\
            Vậy $(%s; %s)$ là một nghiệm của hệ bất phương trình $(I)$.''' 
                             % (tp[0], tp[1], tp[0], tp[1], tp[0]+tp[1], tp[0], tp[1], 2*tp[0]+tp[1], tp[0], tp[1], tp[0]+2*tp[1], tp[0], tp[1], tp[0], tp[1]))

            loigiai_nb_1_s = ('''Thay $x=%s, y=%s$ vào bất phương trình đầu tiên của hệ là $x+y \\ge 12$ ta có: $%s + %s = %s \\ge 12$ (vô lý). \\\\
            Vậy $(%s; %s)$ không là nghiệm của hệ bất phương trình $(I)$.''' 
                             % (fp[0], fp[1], fp[0], fp[1], fp[0]+fp[1], fp[0], fp[1]))

            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình là miền ngũ giác'
            th_da_1_s = 'Miền nghiệm của hệ bất phương trình là miền ' + random.choice(['tứ giác', 'lục giác', 'tam giác'])
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vẽ các đường thẳng $d_1: x+y=12$; $d_2: 2x+y=16$; $d_3: x+2y=14$; $x=12$; $y=12$ và xác định các nửa mặt phẳng thỏa mãn điều kiện.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.4, line width=1pt]
            \\draw[->] (-2, 0) -- (14, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 14) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (14,14);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (14,14);
            \\fill[white] (2,12) -- (4,8) -- (10,2) -- (12,1) -- (12,12) -- cycle;
            \\draw[black] (-2,14) -- (14,-2); 
            \\draw[black] (-1,18) -- (8,0);   
            \\draw[black] (-2,8) -- (16,-1);  
            \\draw[black] (12,-2) -- (12,14); 
            \\draw[black] (-2,12) -- (14,12); 
            \\coordinate (A) at (2,12);
            \\coordinate (B) at (4,8);
            \\coordinate (C) at (10,2);
            \\coordinate (D) at (12,1);
            \\coordinate (E) at (12,12);
            \\fill (A) circle (3.5pt) node[above left] {$A$};
            \\fill (B) circle (3.5pt) node[below left] {$B$};
            \\fill (C) circle (3.5pt) node[below left] {$C$};
            \\fill (D) circle (3.5pt) node[right] {$D$};
            \\fill (E) circle (3.5pt) node[above right] {$E$};
            \\end{tikzpicture}
            \\end{center}
            Miền nghiệm là phần mặt phẳng không bị gạch chéo, là một ngũ giác với các đỉnh $A(2;12), B(4;8), C(10;2), D(12;1), E(12;12)$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Diện tích miền nghiệm của bất phương trình $(I)$ là $67$'
            vd_da_1_s = 'Diện tích miền nghiệm của bất phương trình $(I)$ là $%s$' % random.choice([113, 76, 65, 80])
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi miền nghiệm là ngũ giác $ABCDE$ như hình vẽ trên với $A(2;12), B(4;8), C(10;2), D(12;1), E(12;12)$. \\\\
            Ta tính diện tích ngũ giác này bằng cách lấy diện tích hình chữ nhật giới hạn bởi $x \\in [2;12]$ và $y \\in [0;12]$ trừ đi diện tích phần nằm dưới đường gấp khúc $ABCD$. \\\\
            Diện tích hình chữ nhật là $S_0 = (12 - 2) \\cdot 12 = 120$. \\\\
            Phần nằm dưới đường gấp khúc $ABCD$ gồm $3$ hình thang vuông: \\\\
            $S_1$ (dưới $AB$) $= \\frac{12+8}{2} \\cdot (4 - 2) = 20$. \\\\
            $S_2$ (dưới $BC$) $= \\frac{8+2}{2} \\cdot (10 - 4) = 30$. \\\\
            $S_3$ (dưới $CD$) $= \\frac{2+1}{2} \\cdot (12 - 10) = 3$. \\\\
            Tổng diện tích phần dưới là $S_{duoi} = 20 + 30 + 3 = 53$. \\\\
            Vậy diện tích miền nghiệm là $S = S_0 - S_{duoi} = 120 - 53 = 67$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Với mọi cặp $(x; y)$ thoả mãn hệ bất phương trình $(I)$ thì giá trị nhỏ nhất của biểu thức $F = %sx + %sy$ là $%s$' % (cx, cy, min_val)
            vdc_da_1_s = 'Với mọi cặp $(x; y)$ thoả mãn hệ bất phương trình $(I)$ thì giá trị nhỏ nhất của biểu thức $F = %sx + %sy$ là $%s$' % (cx, cy, false_min_val)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta tính giá trị của biểu thức $F(x;y) = %sx + %sy$ tại các đỉnh của đa giác miền nghiệm: \\\\
            Tại $A(2;12)$: $F(2;12) = %s \\cdot 2 + %s \\cdot 12 = %s$. \\\\
            Tại $B(4;8)$: $F(4;8) = %s \\cdot 4 + %s \\cdot 8 = %s$. \\\\
            Tại $C(10;2)$: $F(10;2) = %s \\cdot 10 + %s \\cdot 2 = %s$. \\\\
            Tại $D(12;1)$: $F(12;1) = %s \\cdot 12 + %s \\cdot 1 = %s$. \\\\
            Tại $E(12;12)$: $F(12;12) = %s \\cdot 12 + %s \\cdot 12 = %s$. \\\\
            Quan sát các giá trị trên, ta thấy giá trị nhỏ nhất của biểu thức là $%s$.''' 
                             % (cx, cy, cx, cy, vals[0], cx, cy, vals[1], cx, cy, vals[2], cx, cy, vals[3], cx, cy, vals[4], min_val))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

            # Lựa chọn lời giải tương ứng
            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = (
                '\\begin{minipage}{\\textwidth}\n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\choiceTFn\n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{\n'
                '\\begin{enumEX}[a)]{1}\n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}}\n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

