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


def bt_dang28_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên
            # Random tham số cho hệ bất phương trình
            # Chọn c_x, c_y sao cho x + 2y - c_1 <= 0 và 2x + y - c_2 <= 0 tạo thành một tứ giác đẹp ở góc phần tư thứ nhất.
            c_1 = random.choice([80, 100, 120])
            c_2 = random.choice([60, 80, 100])

            # Tính tọa độ đỉnh của miền tứ giác OABC
            # Giao điểm của x + 2y = c_1 và 2x + y = c_2
            # x + 2y = c_1 => x = c_1 - 2y
            # 2(c_1 - 2y) + y = c_2 => 2c_1 - 4y + y = c_2 => 3y = 2c_1 - c_2 => y = (2c_1 - c_2) / 3
            # x = c_1 - 2(2c_1 - c_2)/3 = (3c_1 - 4c_1 + 2c_2) / 3 = (2c_2 - c_1) / 3

            # Để giao điểm nằm ở góc phần tư thứ nhất thì 2c_2 > c_1 và 2c_1 > c_2.
            # Ta thiết lập bộ c_1, c_2 thỏa mãn.
            pairs = [(100, 80), (120, 90), (140, 100)]
            c_1, c_2 = random.choice(pairs)
            x_B = int((2*c_2 - c_1) / 3)
            y_B = int((2*c_1 - c_2) / 3)

            # Điểm cho câu Nhận biết
            nb_x = random.choice([20, 30, 40])
            nb_y = random.choice([30, 40, 50])
            while 2*nb_x + nb_y > c_2:
                nb_x = random.choice([10, 15, 20])
                nb_y = random.choice([10, 20, 30])

            nb_x_false = random.choice([50, 60, 70])
            nb_y_false = random.choice([60, 70, 80])
            while 2*nb_x_false + nb_y_false <= c_2:
                nb_x_false += 10

            # Điểm cho câu Thông hiểu
            th_x = random.choice([-1, -2, -3])
            th_y = random.choice([1, 2, 3])

            th_x_true = random.choice([10, 20])
            th_y_true = random.choice([10, 20])

            # Điểm cho câu Vận dụng
            vd_x = random.choice([-1, -2, -3])
            vd_y = random.choice([4, 5, 6])

            vd_x_false = random.choice([15, 25])
            vd_y_false = random.choice([15, 25])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} x + 2y - %s \\le 0 \\\\ 2x + y - %s \\le 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$.''' % (c_1, c_2))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_s = '\\True $(%s; %s)$ là một nghiệm của bất phương trình $2x + y - %s \\le 0$' % (nb_x_false, nb_y_false, c_2)
            nb_da_1_d = '$(%s; %s)$ là một nghiệm của bất phương trình $2x + y - %s \\le 0$' % (nb_x, nb_y, c_2)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1_d = ('''Thay $x = %s, y = %s$ vào bất phương trình $2x + y - %s \\le 0$ ta được: \\\\
            $2 \\cdot %s + %s - %s = %s \\le 0$ (luôn đúng). \\\\
            Vậy $(%s; %s)$ là một nghiệm của bất phương trình $2x + y - %s \\le 0$.''' % (nb_x, nb_y, c_2, nb_x, nb_y, c_2, 2*nb_x+nb_y-c_2, nb_x, nb_y, c_2))

            loigiai_nb_1_s = ('''Thay $x = %s, y = %s$ vào bất phương trình $2x + y - %s \\le 0$ ta được: \\\\
            $2 \\cdot %s + %s - %s = %s \\le 0$ (vô lý). \\\\
            Vậy $(%s; %s)$ không là nghiệm của bất phương trình $2x + y - %s \\le 0$.''' % (nb_x_false, nb_y_false, c_2, nb_x_false, nb_y_false, c_2, 2*nb_x_false+nb_y_false-c_2, nb_x_false, nb_y_false, c_2))

            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_s = '\\True $(%s; %s)$ là một nghiệm của hệ bất phương trình trên' % (th_x, th_y)
            th_da_1_d = '$(%s; %s)$ là một nghiệm của hệ bất phương trình trên' % (th_x_true, th_y_true)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1_d = ('''Thay $x = %s, y = %s$ vào hệ bất phương trình ta được: \\\\
            $\\begin{cases} %s + 2 \\cdot %s - %s = %s \\le 0 \\\\ 2 \\cdot %s + %s - %s = %s \\le 0 \\\\ %s \\ge 0 \\\\ %s \\ge 0 \\end{cases}$ (thỏa mãn). \\\\
            Vậy $(%s; %s)$ là một nghiệm của hệ bất phương trình trên.''' % (th_x_true, th_y_true, th_x_true, th_y_true, c_1, th_x_true+2*th_y_true-c_1, th_x_true, th_y_true, c_2, 2*th_x_true+th_y_true-c_2, th_x_true, th_y_true, th_x_true, th_y_true))

            loigiai_th_1_s = ('''Thay $x = %s, y = %s$ vào bất phương trình $x \\ge 0$ ta thấy không thỏa mãn (vì $%s < 0$). \\\\
            Vậy $(%s; %s)$ không là nghiệm của hệ bất phương trình trên.''' % (th_x, th_y, th_x, th_x, th_y))

            loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $(%s; %s)$ không là một nghiệm của hệ bất phương trình trên' % (vd_x, vd_y)
            vd_da_1_s = '$(%s; %s)$ không là một nghiệm của hệ bất phương trình trên' % (vd_x_false, vd_y_false)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1_d = ('''Thay $x = %s, y = %s$ vào bất phương trình $x \\ge 0$ ta thấy không thỏa mãn (vì $%s < 0$). \\\\
            Vậy $(%s; %s)$ không là một nghiệm của hệ bất phương trình trên.''' % (vd_x, vd_y, vd_x, vd_x, vd_y))

            loigiai_vd_1_s = ('''Thay $x = %s, y = %s$ vào hệ bất phương trình ta được: \\\\
            $\\begin{cases} %s + 2 \\cdot %s - %s = %s \\le 0 \\\\ 2 \\cdot %s + %s - %s = %s \\le 0 \\\\ %s \\ge 0 \\\\ %s \\ge 0 \\end{cases}$ (thỏa mãn). \\\\
            Vậy $(%s; %s)$ là một nghiệm của hệ bất phương trình trên.''' % (vd_x_false, vd_y_false, vd_x_false, vd_y_false, c_1, vd_x_false+2*vd_y_false-c_1, vd_x_false, vd_y_false, c_2, 2*vd_x_false+vd_y_false-c_2, vd_x_false, vd_y_false, vd_x_false, vd_y_false))

            loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Miền nghiệm của hệ bất phương trình trên là một miền tứ giác'
            vdc_da_1_s = 'Miền nghiệm của hệ bất phương trình trên là một miền tam giác'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            # Điểm giao của x+2y=c_1 với Ox là (c_1, 0), Oy là (0, c_1/2)
            # Điểm giao của 2x+y=c_2 với Ox là (c_2/2, 0), Oy là (0, c_2)
            x_A = int(c_2/2)
            y_C = int(c_1/2)

            loigiai_vdc_1 = ('''Vẽ các đường thẳng $d_1: x+2y-%s=0$, $d_2: 2x+y-%s=0$, $x=0$, $y=0$ trên cùng một mặt phẳng tọa độ và xác định các nửa mặt phẳng thỏa mãn.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.08, line width=1pt]
            \\draw[->] (-10, 0) -- (%s, 0) node[below] {$x$};
            \\draw[->] (0, -10) -- (0, %s) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-10,-10) rectangle (%s,%s);
            \\fill[pattern=north east lines, pattern color=black] (-10,-10) rectangle (%s,%s);
            \\fill[white] (0,0) -- (%s,0) -- (%s,%s) -- (0,%s) -- cycle;
            \\draw[black] (0,%s) -- (%s,0); 
            \\draw[black] (0,%s) -- (%s,0);  
            \\draw[black] (0,-10) -- (0,%s); 
            \\draw[black] (-10,0) -- (%s,0); 
            \\coordinate (A) at (%s,0);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (0,%s);
            \\fill (0,0) circle (15pt);
            \\fill (A) circle (15pt) node[below] {$%s$};
            \\fill (B) circle (15pt);
            \\fill (C) circle (15pt) node[left] {$%s$};
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[left] {$%s$};
            \\end{tikzpicture}
            \\end{center}
            Miền nghiệm của hệ bất phương trình là miền tứ giác $OABC$ với $O(0;0), A(%s;0), B(%s;%s), C(0;%s)$.''' % 
            (c_1, c_2, 
             c_1+20, c_2+20, 
             c_1+20, c_2+20, 
             c_1+20, c_2+20,
             x_A, x_B, y_B, y_C,
             c_1/2, c_1,
             c_2, c_2/2,
             c_2+20, c_1+20,
             x_A, x_B, y_B, y_C,
             x_A, y_C,
             x_B, x_B, x_B, y_B, y_B, y_B,
             x_A, x_B, y_B, y_C))

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

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Lấy lại lời giải tương ứng
            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
            loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
            loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s

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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

