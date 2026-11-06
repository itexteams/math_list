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


def bt_dang31_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')
            p1_val = random.choice([24, 25, 26, 28])
            p2_val = random.choice([20, 21, 22, 23])
            min_p_val = random.choice([50, 56, 60])
            max_p_val = random.choice([90, 91, 100])
            c1_val = random.choice([20, 23, 25])
            c2_val = random.choice([5, 7, 10])

            # Tìm điểm True
            while True:
                x_t = randint(1, 3)
                y_t = randint(x_t, 5)
                if min_p_val <= p1_val * x_t + p2_val * y_t <= max_p_val:
                    break

            # Tìm điểm False
            while True:
                x_f = randint(2, 5)
                y_f = randint(0, x_f - 1)
                break

            # Điểm cực trị
            x_opt = Rational(min_p_val, p1_val + p2_val)

            # Tính toán tọa độ phục vụ vẽ TikZ
            xA_val = float(min_p_val / (p1_val + p2_val))
            yA_val = float(min_p_val / (p1_val + p2_val))
            xB_val = 0.0
            yB_val = float(min_p_val / p2_val)
            xC_val = 0.0
            yC_val = float(max_p_val / p2_val)
            xD_val = float(max_p_val / (p1_val + p2_val))
            yD_val = float(max_p_val / (p1_val + p2_val))

            # Mã TikZ hình vẽ miền nghiệm phong cách đen trắng
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1.2, line width=1pt]
            \\draw[->] (-1, 0) -- (4, 0) node[below] {$x$};
            \\draw[->] (0, -1) -- (0, 6) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-1,-1) rectangle (4,6);
            \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle (4,6);
            \\fill[white] (%.2f,%.2f) -- (0,%.2f) -- (0,%.2f) -- (%.2f,%.2f) -- cycle;
            \\draw[black] (-1, %.2f) -- (4, %.2f);
            \\draw[black] (-1, %.2f) -- (4, %.2f);
            \\draw[black] (-1, -1) -- (4, 4);
            \\coordinate (A) at (%.2f,%.2f);
            \\coordinate (B) at (0,%.2f);
            \\coordinate (C) at (0,%.2f);
            \\coordinate (D) at (%.2f,%.2f);
            \\fill (A) circle (0.5pt) node[right] {$A$};
            \\fill (B) circle (0.5pt) node[left] {$B$};
            \\fill (C) circle (0.5pt) node[left] {$C$};
            \\fill (D) circle (0.5pt) node[above right] {$D$};
            \\end{tikzpicture}
            \\end{center}''' % (
                xA_val, yA_val, yB_val, yC_val, xD_val, yD_val,
                (min_p_val + p1_val)/p2_val, (min_p_val - 4*p1_val)/p2_val,
                (max_p_val + p1_val)/p2_val, (max_p_val - 4*p1_val)/p2_val,
                xA_val, yA_val, yB_val, yC_val, xD_val, yD_val
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong $1$ lạng thịt bò chứa $%s$ g protein, $1$ lạng cá chứa $%s$ g protein. Trung bình trong một ngày, một người đàn ông cần từ $%s$ đến $%s$ g protein. Theo lời khuyên của bác sĩ, để tốt cho sức khỏe thì không nên ăn thịt nhiều hơn cá. Gọi $x, y$ lần lượt là số lạng thịt bò, lạng cá mà một người đàn ông ăn trong một ngày. Biết giá mỗi lạng thịt bò là $%s$ nghìn đồng, giá mỗi lạng cá là $%s$ nghìn đồng. \\\\
            ''' % (latex(p1_val), latex(p2_val), latex(min_p_val), latex(max_p_val), latex(c1_val), latex(c2_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hệ bất phương trình bậc nhất hai ẩn $x, y$ biểu diễn lượng protein cần thiết là $\\left\\{\\begin{matrix} %sx + %sy \\ge %s \\\\ %sx + %sy \\le %s \\\\ x \\le y \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{matrix}\\right.$' % (latex(p1_val), latex(p2_val), latex(min_p_val), latex(p1_val), latex(p2_val), latex(max_p_val))
            nb_da_1_s = 'Hệ bất phương trình bậc nhất hai ẩn $x, y$ biểu diễn lượng protein cần thiết là $\\left\\{\\begin{matrix} %sx + %sy \\ge %s \\\\ %sx + %sy \\le %s \\\\ x \\ge y \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{matrix}\\right.$' % (latex(p1_val), latex(p2_val), latex(min_p_val), latex(p1_val), latex(p2_val), latex(max_p_val))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Theo giả thiết, số protein cung cấp từ $x$ lạng thịt bò và $y$ lạng cá là $%sx + %sy$. \\\\
            Lượng protein cần thiết nằm trong khoảng từ $%s$ đến $%s$ nên: $\\left\\{\\begin{matrix} %sx + %sy \\ge %s \\\\ %sx + %sy \\le %s \\end{matrix}\\right.$. \\\\
            Không nên ăn thịt nhiều hơn cá nên $x \\le y$. \\\\
            Số lượng thức ăn không thể âm nên $x \\ge 0, y \\ge 0$. \\\\
            Vậy hệ bất phương trình là $\\left\\{\\begin{matrix} %sx + %sy \\ge %s \\\\ %sx + %sy \\le %s \\\\ x \\le y \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{matrix}\\right.$.'''
                        % (latex(p1_val), latex(p2_val), latex(min_p_val), latex(max_p_val), latex(p1_val), latex(p2_val), latex(min_p_val), latex(p1_val), latex(p2_val), latex(max_p_val), latex(p1_val), latex(p2_val), latex(min_p_val), latex(p1_val), latex(p2_val), latex(max_p_val)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Điểm $M(%s; %s)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x, y$ biểu diễn lượng protein cần thiết' %(latex(x_t), latex(y_t))  
            th_da_1_s = 'Điểm $M(%s; %s)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x, y$ biểu diễn lượng protein cần thiết' %(latex(x_f), latex(y_f))  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Để kiểm tra một điểm có thuộc miền nghiệm hay không, ta thay tọa độ $M(x;y)$ vào hệ bất phương trình. \\\\
            Nếu thỏa mãn tất cả các bất phương trình trong hệ thì điểm đó thuộc miền nghiệm, ngược lại thì không.''')

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Chi phí mua thịt bò và cá là $T(x; y) = %sx + %sy$' % (latex(c1_val), latex(c2_val))  
            vd_da_1_s = 'Chi phí mua thịt bò và cá là $T(x; y) = %sx + %sy$' % (latex(c2_val), latex(c1_val))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Giá mỗi lạng thịt bò là $%s$ nghìn đồng, giá mỗi lạng cá là $%s$ nghìn đồng. \\\\
            Vậy hàm chi phí là $T(x; y) = %sx + %sy$.'''  
                       %(latex(c1_val), latex(c2_val), latex(c1_val), latex(c2_val)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Chi phí mua thịt bò và cá thấp nhất khi $x = %s; y = %s$' %(latex(x_opt), latex(x_opt)) 
            vdc_da_1_s = 'Chi phí mua thịt bò và cá thấp nhất khi $x = %s; y = %s$' %(latex(Rational(max_p_val, p1_val+p2_val)), latex(Rational(max_p_val, p1_val+p2_val))) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Miền nghiệm của hệ bất phương trình là miền tứ giác $ABCD$ (kể cả biên) như hình vẽ dưới đây: \\\\
            %s
            Hàm chi phí $T(x; y) = %sx + %sy$ đạt giá trị nhỏ nhất tại một trong các đỉnh của đa giác miền nghiệm. \\\\
            Dựa vào đồ thị và tọa độ các đỉnh, giá trị nhỏ nhất đạt được tại giao điểm $A$ của đường thẳng $x = y$ và đường thẳng $%sx + %sy = %s$. \\\\
            Giải hệ phương trình $\\left\\{\\begin{matrix} x = y \\\\ %sx + %sy = %s \\end{matrix}\\right. \\Leftrightarrow x = y = %s$. \\\\
            Vậy chi phí thấp nhất khi $x = %s; y = %s$.'''
                       %(tikz_code, latex(c1_val), latex(c2_val), latex(p1_val), latex(p2_val), latex(min_p_val), latex(p1_val), latex(p2_val), latex(min_p_val), latex(x_opt), latex(x_opt), latex(x_opt)))

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
            str(noidungcauhoi)+ 
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

