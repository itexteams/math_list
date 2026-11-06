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


def bt_dang23_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số để tạo hàm bậc 3 dạng y = ax^3 + bx^2 + cx + d
            # Để đảm bảo tính nguyên của các hệ số, ta chọn khéo các điểm cực trị
            a_val = random.randint(-2, -1) # Hàm số có a < 0 theo dạng bảng biến thiên mẫu
            case = random.randint(1, 2)
            if case == 1:
                x1_val = random.randint(-3, -1) * 2
                x2_val = 0
            else:
                x1_val = 0
                x2_val = random.randint(1, 3) * 2

            b_val = -3 * a_val * (x1_val + x2_val) // 2
            c_val = 3 * a_val * x1_val * x2_val
            d_val = random.randint(-5, 5)

            y1_val = a_val * x1_val**3 + b_val * x1_val**2 + c_val * x1_val + d_val
            y2_val = a_val * x2_val**3 + b_val * x2_val**2 + c_val * x2_val + d_val

            # Đóng khung Bảng biến thiên bằng TikZ
            bbt_tikz = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$y'$/0.7,$y$/2.1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,-,0,+,0,-}
            \\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$}
            \\end{tikzpicture}
            \\end{center}''' %(latex(x1_val), latex(x2_val), latex(y1_val), latex(y2_val)))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ ($a,b,c,d \\in \\mathbb{R}$) có bảng biến thiên như hình vẽ dưới đây:
            %s''' %(bbt_tikz))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số không có giá trị lớn nhất trên $\\mathbb{R}$'
            nb_da_1_s = 'Hàm số đạt giá trị lớn nhất là $%s$' %(latex(y2_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Quan sát bảng biến thiên, ta thấy $\\lim\\limits_{x \\to -\\infty} y = +\\infty$ nên hàm số không có giá trị lớn nhất trên $\\mathbb{R}$. \\\\
            Giá trị $%s$ chỉ là cực đại của hàm số.''' %(latex(y2_val)))

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
            m_true = y1_val + 1
            m_false = y2_val + 1
            th_da_1_d = '\\True Đường thẳng $y = %s$ cắt đồ thị hàm số tại ba điểm phân biệt' %(latex(m_true))
            th_da_1_s = 'Đường thẳng $y = %s$ cắt đồ thị hàm số tại ba điểm phân biệt' %(latex(m_false))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Từ bảng biến thiên, ta thấy giá trị cực tiểu là $y_{CT} = %s$ và giá trị cực đại là $y_{CD} = %s$. \\\\
            Để đường thẳng $y = m$ cắt đồ thị hàm số tại ba điểm phân biệt thì $%s < m < %s$. \\\\
            Do đó đường thẳng $y = %s$ cắt đồ thị tại ba điểm phân biệt.'''
                            %(latex(y1_val), latex(y2_val), latex(y1_val), latex(y2_val), latex(m_true)))

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
            neg_count = sum(1 for v in [a_val, b_val, c_val, d_val] if v < 0)
            wrong_count = neg_count + 1 if neg_count < 4 else neg_count - 1

            vd_da_1_d = '\\True Trong bốn hệ số $a, b, c, d$ có đúng $%s$ số âm' %(latex(neg_count))
            vd_da_1_s = 'Trong bốn hệ số $a, b, c, d$ có đúng $%s$ số âm' %(latex(wrong_count))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ bảng biến thiên, ta có đồ thị hàm số đạt cực trị tại $x = %s$ và $x = %s$. \\\\
            Giá trị cực trị tương ứng là $f(%s) = %s$ và $f(%s) = %s$. \\\\
            Ta có $y' = 3ax^2 + 2bx + c$. Ta có hệ phương trình: \\\\
            $\\left\\{\\begin{matrix} 3a(%s)^2 + 2b(%s) + c = 0 \\\\ 3a(%s)^2 + 2b(%s) + c = 0 \\\\ a(%s)^3 + b(%s)^2 + c(%s) + d = %s \\\\ a(%s)^3 + b(%s)^2 + c(%s) + d = %s \\end{matrix}\\right.$ \\\\
            Giải hệ phương trình ta được $a = %s, b = %s, c = %s, d = %s$. \\\\
            Vậy trong bốn hệ số có đúng $%s$ số âm.''' %(
                latex(x1_val), latex(x2_val),
                latex(x1_val), latex(y1_val), latex(x2_val), latex(y2_val),
                latex(x1_val), latex(x1_val),
                latex(x2_val), latex(x2_val),
                latex(x1_val), latex(x1_val), latex(x1_val), latex(y1_val),
                latex(x2_val), latex(x2_val), latex(x2_val), latex(y2_val),
                latex(a_val), latex(b_val), latex(c_val), latex(d_val), latex(neg_count)
            ))

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
            xp = x2_val + 1
            yp = a_val * xp**3 + b_val * xp**2 + c_val * xp + d_val

            vdc_da_1_d = '\\True Đồ thị hàm số đi qua điểm $\\left(%s; %s\\right)$' %(latex(xp), latex(yp))
            vdc_da_1_s = 'Đồ thị hàm số đi qua điểm $\\left(%s; %s\\right)$' %(latex(xp), latex(yp + 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            f_expr = a_val*x**3 + b_val*x**2 + c_val*x + d_val
            f_latex = latex(f_expr)
            loigiai_vdc_1 = ('''Từ câu trên, ta có hàm số là $y = %s$. \\\\
            Thay $x = %s$ vào hàm số, ta được $y = %s$. \\\\
            Vậy đồ thị hàm số đi qua điểm $\\left(%s; %s\\right)$.''' %(
                f_latex, latex(xp), latex(yp), latex(xp), latex(yp)
            ))

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

