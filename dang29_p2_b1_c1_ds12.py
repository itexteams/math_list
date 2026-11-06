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


def bt_dang29_p2_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # Random các tham số
            # Đồ thị hàm bậc 3 dạng y = ax^3 + bx^2 + cx + d
            # Các điểm cực trị có tọa độ nguyên
            while True:
                x_ct1 = 0
                x_ct2 = random.randint(1, 3)

                y_ct1 = random.randint(-5, -2)
                y_ct2 = 0

                # Tính diện tích tam giác tạo bởi đt qua 2 điểm cực trị và 2 trục tọa độ
                # pt: (y - y1)/(y2 - y1) = (x - x1)/(x2 - x1)
                # y = m*x + c
                if x_ct2 != x_ct1:
                    m = Rational(y_ct2 - y_ct1, x_ct2 - x_ct1)
                    c = y_ct1 - m * x_ct1

                    # giao điểm với Ox: y=0 => x = -c/m
                    if m != 0:
                        x_giao = -c/m
                        S = Rational(abs(x_giao * c), 2)
                        break

            # Tính các hệ số của hàm bậc 3 để vẽ TikZ: f(x) = ax^3 + bx^2 + c
            a_val = round(2 * y_ct1 / (x_ct2**3), 4)
            b_val = round(-3 * y_ct1 / (x_ct2**2), 4)
            c_val = round(y_ct1, 4)

            # Xác định vùng vẽ đồ thị (Domain) cho đẹp
            xmin_val = min(-1.5, -x_ct2/2 - 0.5)
            xmax_val = max(3.5, x_ct2 + 1.5)
            ymin_val = y_ct1 - 1.5
            ymax_val = 1.5

            # Nội dung câu hỏi (TikZ sinh động theo tham số)
            noidungcauhoi = f'''Cho hàm số $y=f(x)$ xác định, liên tục trên $\\mathbb{{R}}$ và có đồ thị là đường cong trong hình vẽ bên.
            \\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.8, thick]
            \\draw[->] ({xmin_val:.1f},0) -- ({xmax_val:.1f},0) node[below] {{$x$}};
            \\draw[->] (0,{ymin_val:.1f}) -- (0,{ymax_val:.1f}) node[right] {{$y$}};
            \\node at (0.2,0.2) {{$0$}};'''

            # Vẽ tick cho trục x
            for i in range(math.floor(xmin_val)+1, math.ceil(xmax_val)):
                if i != 0:
                    noidungcauhoi += f"                \\draw ({i},0) node[above] {{${i}$}};\n"
                    noidungcauhoi += f"                \\draw ({i},-0.1) -- ({i},0.1);\n"

            # Vẽ tick cho trục y
            for i in range(math.floor(ymin_val)+1, math.ceil(ymax_val)):
                if i != 0:
                    noidungcauhoi += f"                \\draw (0,{i}) node[left] {{${i}$}};\n"
                    noidungcauhoi += f"                \\draw (-0.1,{i}) -- (0.1,{i});\n"

            # Vẽ đồ thị hàm số (Thêm scope và clip để giới hạn vùng vẽ)
            noidungcauhoi += f"                \\begin{{scope}}\n"
            # Giới hạn vùng cắt bên trong các mũi tên trục tọa độ một chút để không bị lẹm
            noidungcauhoi += f"                \\clip ({xmin_val+0.1:.2f}, {ymin_val+0.1:.2f}) rectangle ({xmax_val-0.1:.2f}, {ymax_val-0.1:.2f});\n"
            # Mở rộng domain ra ngoài để đồ thị luôn chạm tới mép của khung clip
            noidungcauhoi += f"                \\draw[smooth, samples=150, domain={xmin_val-0.5:.2f}:{xmax_val+0.5:.2f}] plot(\\x, {{{a_val}*(\\x)^3 + {b_val}*(\\x)^2 + {c_val}}});\n"
            noidungcauhoi += f"                \\end{{scope}}\n"

            noidungcauhoi += '''                \\end{tikzpicture}
            \\end{center}'''

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_s = '\\True Đồ thị hàm số có hai điểm cực trị là $(%s;%s)$ và $(%s;%s)$' % (latex(x_ct2), latex(y_ct2), latex(y_ct1), latex(x_ct1))
            nb_da_1_d = 'Đồ thị hàm số có hai điểm cực trị là $(%s;%s)$ và $(%s;%s)$' % (latex(x_ct2), latex(y_ct2), latex(x_ct1), latex(y_ct1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào đồ thị, hàm số đạt cực trị tại các điểm có toạ độ là $(%s; %s)$ và $(%s; %s)$.''' % (latex(x_ct2), latex(y_ct2), latex(x_ct1), latex(y_ct1)))

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
            th_da_1_d = '\\True Hàm số đồng biến trên khoảng $(%s; %s)$' % (latex(x_ct1), latex(x_ct2))
            th_da_1_s = 'Hàm số đồng biến trên khoảng $(-%s; %s)$' % (latex(x_ct1+1), latex(x_ct2))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Dựa vào đồ thị, trong khoảng $(%s; %s)$ đồ thị hàm số đi lên từ trái sang phải nên hàm số đồng biến trên khoảng này.''' % (latex(x_ct1), latex(x_ct2)))

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
            vd_da_1_d = '\\True $f\'(x) < 0$ khi $x \\in (-\\infty; %s) \\cup (%s; +\\infty)$' % (latex(x_ct1), latex(x_ct2))
            vd_da_1_s = '$f\'(x) < 0$ khi $x \\in (-\\infty; %s) \\cup (%s; +\\infty)$' % (latex(x_ct1-1), latex(x_ct2))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ đồ thị ta thấy hàm số nghịch biến trên các khoảng $(-\\infty; %s)$ và $(%s; +\\infty)$, suy ra $f'(x) < 0$ với mọi $x \\in (-\\infty; %s) \\cup (%s; +\\infty)$.''' % (latex(x_ct1), latex(x_ct2), latex(x_ct1), latex(x_ct2)))

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
            vdc_da_1_d = '\\True Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $y=f(x)$ tạo với hai trục toạ độ một tam giác có diện tích $S$ bằng $%s$ (đvdt)' % (latex(S))
            vdc_da_1_s = 'Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $y=f(x)$ tạo với hai trục toạ độ một tam giác có diện tích $S$ bằng $%s$ (đvdt)' % (latex(S+2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Hai điểm cực trị của đồ thị hàm số là $A(%s; %s)$ và $B(%s; %s)$. \\\\
            Đường thẳng đi qua $A$ và $B$ có hệ số góc $k = \\frac{%s - (%s)}{%s - %s} = %s$. \\\\
            Phương trình đường thẳng $AB$: $y = %s(x - %s) + %s \\Rightarrow y = %s x + %s$. \\\\
            Gọi $M, N$ lần lượt là giao điểm của đường thẳng $AB$ với trục tung, trục hoành. \\\\
            Toạ độ điểm $M(0; %s)$, $N(%s; 0)$. \\\\
            Diện tích tam giác $OMN$ là $S = \\frac{1}{2} OM \\cdot ON = \\frac{1}{2} |%s| \\cdot |%s| = %s$ (đvdt).''' % (latex(x_ct1), latex(y_ct1), latex(x_ct2), latex(y_ct2), latex(y_ct2), latex(y_ct1), latex(x_ct2), latex(x_ct1), latex(m), latex(m), latex(x_ct2), latex(y_ct2), latex(m), latex(c), latex(c), latex(x_giao), latex(c), latex(x_giao), latex(S)))

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

