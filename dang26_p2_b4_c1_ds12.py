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


def bt_dang26_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các hệ số
            while True:
                c = random.choice([-1, 1])
                a = random.choice([-2, -1, 1, 2, 3])
                k = random.choice([-3, -2, -1, 1, 2, 3]) # k = -b/a => b = -k*a
                b = -k * a

                x0 = -1 // c # Tiệm cận đứng x = -1/c
                y0 = a // c  # Tiệm cận ngang y = a/c

                # Tử số đạo hàm
                D = a - b * c

                # Các giao điểm với trục toạ độ
                x_int = k
                y_int = b

                # Điều kiện để đồ thị không suy biến, các điểm không bị trùng lặp để vẽ hình đẹp
                if D != 0 and x_int != x0 and y_int != y0 and x_int != 0 and y_int != 0 and abs(x0) <= 3 and abs(y0) <= 3 and abs(x_int) <= 3 and abs(y_int) <= 3:
                    break

            sign_str = "<" if D < 0 else ">"
            opp_sign_str = ">" if D < 0 else "<"
            monotony = "nghịch" if D < 0 else "đồng"
            opp_monotony = "đồng" if D < 0 else "nghịch"

            S_d = a + b + c
            S_s = a + b + c + random.choice([-2, -1, 1, 2])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=f(x)=\\frac{ax+b}{cx+1}$ với $a,b,c \\in \\mathbb{R}$ có đồ thị như hình vẽ dưới: \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8]
            \\draw[->] (-4,0) -- (4,0) node[below] {$x$};
            \\draw[->] (0,-4) -- (0,4) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\draw[dashed] (%s,-4) -- (%s,4);
            \\draw[dashed] (-4,%s) -- (4,%s);
            \\fill (%s, 0) circle (0.5pt) node[below left] {$%s$};
            \\fill (0, %s) circle (0.5pt) node[below right] {$%s$};
            \\fill (%s, 0) circle (0.5pt) node[above right] {$%s$};
            \\fill (0, %s) circle (0.5pt) node[above left] {$%s$};
            \\clip (-4,-4) rectangle (4,4);
            \\draw[thick, samples=100, smooth, domain=-4:%s] plot (\\x, {(%s*\\x+(%s))/(%s*\\x+1)});
            \\draw[thick, samples=100, smooth, domain=%s:4] plot (\\x, {(%s*\\x+(%s))/(%s*\\x+1)});
            \\end{tikzpicture}
            \\end{center}''' 
                             % (x0, x0, y0, y0, x0, x0, y0, y0, x_int, x_int, y_int, y_int, x0 - 0.1, a, b, c, x0 + 0.1, a, b, c))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đạo hàm: $f\'(x) %s 0, \\forall x \\in \\mathbb{R} \\setminus \\{%s\\}$' % (sign_str, x0)
            nb_da_1_s = 'Đạo hàm: $f\'(x) %s 0, \\forall x \\in \\mathbb{R} \\setminus \\{%s\\}$' % (opp_sign_str, x0)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào đồ thị hàm số ta thấy đồ thị hàm số có hướng đi từ trái sang phải là đi %s trên các khoảng xác định, do đó hàm số %s biến. Suy ra $f'(x) %s 0, \\forall x \\in \\mathbb{R} \\setminus \\{%s\\}$.''' 
                            % ("xuống" if D < 0 else "lên", monotony, sign_str, x0))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hàm số $y=f(x)$ %s biến trên khoảng $(-\\infty; %s)$ và $(%s; +\\infty)$' % (monotony, x0, x0)
            th_da_1_s = 'Hàm số $y=f(x)$ %s biến trên khoảng $(-\\infty; %s)$ và $(%s; +\\infty)$' % (opp_monotony, x0, x0)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Từ đồ thị hàm số, ta thấy hàm số %s biến trên các khoảng $(-\\infty; %s)$ và $(%s; +\\infty)$.''' 
                            % (monotony, x0, x0))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Đồ thị hàm số $y=f(x)$ có đường tiệm cận đứng là $x=%s$ và đường tiệm cận ngang là $y=%s$' % (x0, y0)
            vd_da_1_s = 'Đồ thị hàm số $y=f(x)$ có đường tiệm cận đứng là $y=%s$ và đường tiệm cận ngang là $x=%s$' % (y0, x0)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ đồ thị hàm số, ta thấy đồ thị có đường tiệm cận đứng là $x=%s$ và đường tiệm cận ngang là $y=%s$.''' 
                            % (x0, y0))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Tổng $a+b+c=%s$' % (S_d)
            vdc_da_1_s = 'Tổng $a+b+c=%s$' % (S_s)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Dựa vào đồ thị hàm số, ta có: \\\\
            - Đồ thị có đường tiệm cận đứng $x = -\\frac{1}{c} = %s \\Rightarrow c = %s$. \\\\
            - Đồ thị có đường tiệm cận ngang $y = \\frac{a}{c} = %s \\Rightarrow \\frac{a}{%s} = %s \\Rightarrow a = %s$. \\\\
            - Đồ thị cắt trục tung tại điểm $(0; %s) \\Rightarrow \\frac{a \\cdot 0 + b}{c \\cdot 0 + 1} = %s \\Rightarrow b = %s$. \\\\
            Vậy $a+b+c = %s + (%s) + (%s) = %s$.''' 
                             % (x0, c, y0, c, y0, a, y_int, y_int, b, a, b, c, S_d))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
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
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

