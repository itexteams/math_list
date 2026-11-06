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


def bt_dang8_p2_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo các biến và hằng số từ đồ thị
            ten_ham = 'f'
            ct_ham = '\\frac{ax^2+bx+c}{mx+n}'

            # Sinh các giá trị nhiễu ngẫu nhiên cho các phương án sai
            tc_dung_sai = random.choice([-2, 0, 1, 3])
            tc_xien_sai = random.choice(['x - 1', 'x + 2', '2x + 1'])
            diem_cuc_sai = random.choice(['(1;5)', '(3;1)', '(2;3)'])
            min_val_sai = random.choice([1, 2, 3, 4])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = %s$ ($a \\neq 0, m \\neq 0$) với $a, b, c, m, n$ là các số thực và đồ thị có dạng như hình vẽ sau. \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.7]
            \\draw[->, line width=1pt] (-2.5,0) -- (6.5,0) node[below] {$x$};
            \\draw[->, line width=1pt] (0,-1.5) -- (0,7.5) node[left] {$y$};
            \\draw (0,0) node[below left] {$O$};
            \\foreach \\x in {-2,-1,1,2,3,4,5} \\draw[line width=1pt] (\\x,0.1) -- (\\x,-0.1);
            \\node[below] at (-2,0) {$-2$};
            \\node[below] at (-1,0) {$-1$};
            \\node[below] at (1,0) {$1$};
            \\node[below right] at (2,0) {$2$};
            \\node[below] at (3,0) {$3$};
            \\node[below] at (4,0) {$4$};
            \\node[below] at (5,0) {$5$};
            \\foreach \\y in {-1,1,2,3,4,5,6} \\draw[line width=1pt] (0.1,\\y) -- (-0.1,\\y);
            \\node[left] at (0,-1) {$-1$};
            \\node[left] at (0,1) {$1$};
            \\node[left] at (0,2) {$2$};
            \\node[left] at (0,3) {$3$};
            \\node[left] at (0,5) {$5$};
            \\node[left] at (0,6) {$6$};
            \\draw[line width=1pt] (2,-1.5) -- (2,7.5);
            \\node[above, rotate=90] at (1.7,5.5) {$x = 2$};
            \\draw[line width=1pt, domain=-2.5:5.8] plot (\\x, {\\x+1});
            \\node[below right] at (4.5,5.2) {$y = x + 1$};
            \\draw[dashed, line width=1pt] (0,3) -- (2,3) node[right] {$I$};
            \\draw[dashed, line width=1pt] (1,0) -- (1,1);
            \\draw[dashed, line width=1pt] (3,0) -- (3,5) -- (0,5);
            \\fill (1,1) circle (2pt);
            \\fill (3,5) circle (2pt);
            \\fill (2,3) circle (2pt);
            \\clip (-2.5,-1.5) rectangle (6.5,7.5);
            \\draw[samples=200, domain=-2.5:1.8, line width=1pt] plot (\\x, {\\x + 1 + 1/(\\x-2)});
            \\draw[samples=200, domain=2.2:6.2, line width=1pt] plot (\\x, {\\x + 1 + 1/(\\x-2)});
            \\end{tikzpicture}
            \\end{center}''' % (ct_ham))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $y = %s(x)$ đồng biến trên các khoảng $(-\\infty;1)$ và $(3;+\\infty)$, nghịch biến trên các khoảng $(1;2)$ và $(2;3)$' % (ten_ham)
            nb_da_1_s = 'Hàm số $y = %s(x)$ nghịch biến trong khoảng $(-\\infty;1)$ và $(3;+\\infty)$, đồng biến trong khoảng $(1;2)$ và $(2;3)$' % (ten_ham)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào đồ thị hàm số, ta thấy trên các khoảng $(-\\infty;1)$ và $(3;+\\infty)$ đồ thị đi lên từ trái sang phải nên hàm số đồng biến. Trên các khoảng $(1;2)$ và $(2;3)$ đồ thị đi xuống từ trái sang phải nên hàm số nghịch biến.''' )

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
            th_da_1_d = '\\True Đồ thị hàm số $y = %s(x)$ có tiệm cận đứng là $x = 2$ và tiệm cận xiên là $y = x + 1$' % (ten_ham)
            th_da_1_s = 'Đồ thị hàm số $y = %s(x)$ có tiệm cận đứng là $x = %s$ và tiệm cận xiên là $y = %s$' % (ten_ham, tc_dung_sai, tc_xien_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Quan sát đồ thị, ta thấy đường thẳng tiệm cận đứng song song với trục tung cắt trục hoành tại điểm có hoành độ bằng $2$, do đó tiệm cận đứng là $x = 2$. Đường thẳng tiệm cận xiên đi qua các điểm $(0;1)$ và $(-1;0)$ nên có phương trình là $y = x + 1$.''' )

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
            vd_da_1_d = '\\True Đồ thị hàm số $y = %s(x)$ có điểm cực đại $(1;1)$ và điểm cực tiểu $(3;5)$' % (ten_ham)
            vd_da_1_s = 'Đồ thị hàm số $y = %s(x)$ có điểm cực đại %s và điểm cực tiểu $(3;5)$' % (ten_ham, diem_cuc_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dựa vào dáng điệu của đồ thị hàm số, điểm nhô lên cao nhất của nhánh bên trái có tọa độ $(1;1)$ là điểm cực đại của đồ thị hàm số. Điểm lõm xuống thấp nhất của nhánh bên phải có tọa độ $(3;5)$ là điểm cực tiểu của đồ thị hàm số.''' )

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
            vdc_da_1_d = '\\True Trên khoảng $(2;+\\infty)$, hàm số $y = %s(x)$ có giá trị nhỏ nhất bằng $5$' % (ten_ham)
            vdc_da_1_s = 'Trên khoảng $(2;+\\infty)$, hàm số $y = %s(x)$ có giá trị nhỏ nhất bằng $%s$' % (ten_ham, min_val_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét trên khoảng $(2;+\\infty)$, đồ thị hàm số đi từ $+\\infty$ xuống điểm cực tiểu $(3;5)$ rồi đi lên $+\\infty$. Do đó, giá trị nhỏ nhất của hàm số trên khoảng này đạt được tại điểm cực tiểu, tức là $\\min\\limits_{(2;+\\infty)} f(x) = f(3) = 5$.''' )

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

