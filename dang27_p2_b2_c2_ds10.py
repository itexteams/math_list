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


def bt_dang27_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên
            # Lựa chọn ngẫu nhiên lợi nhuận của rau (c_x) và hoa (c_y) sao cho giá trị lớn nhất luôn đạt được tại điểm B(6; 2)
            pairs = [(3, 4), (4, 5), (5, 6), (5, 7), (7, 9), (7, 10), (8, 11)]
            c_x, c_y = random.choice(pairs)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một gia đình định trồng rau và hoa trên diện tích $8$ ha. Nếu trồng rau thì cần $20$ công và thu lợi $%s$ triệu đồng trên mỗi ha, còn trồng hoa thì cần $30$ công và thu lợi $%s$ triệu đồng trên mỗi ha. Biết số công không được quá $180$. Gọi $x, y$ ($x, y \\in \\mathbb{N}$) lần lượt là số ha rau và hoa trồng được.''' % (c_x, c_y))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Bất phương trình mô tả số công để trồng rau và hoa là $2x + 3y \\le 18$'
            nb_da_1_s = 'Bất phương trình mô tả số công để trồng rau và hoa là $3x + 2y \\le 18$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số công cần để trồng $x$ ha rau là $20x$. \\\\
            Số công cần để trồng $y$ ha hoa là $30y$. \\\\
            Tổng số công là $20x + 30y$. \\\\
            Vì số công không quá $180$ nên ta có bất phương trình: $20x + 30y \\le 180 \\Leftrightarrow 2x + 3y \\le 18$.''')

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
            th_da_1_d = '\\True Tiền thu được khi gia đình trồng rau và hoa là $T = %sx + %sy$' % (c_x, c_y)
            th_da_1_s = 'Tiền thu được khi gia đình trồng rau và hoa là $T = %sx + %sy$' % (c_y, c_x)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Số tiền thu lợi từ $x$ ha rau là $%sx$ (triệu đồng). \\\\
            Số tiền thu lợi từ $y$ ha hoa là $%sy$ (triệu đồng). \\\\
            Tổng số tiền thu được là $T = %sx + %sy$ (triệu đồng).''' % (c_x, c_y, c_x, c_y))

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
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình $\\begin{cases} x + y \\le 8 \\\\ 2x + 3y \\le 18 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$ là tứ giác $OABC$ với $A(8;0), B(6;2), C(0;6)$'
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình $\\begin{cases} x + y \\le 8 \\\\ 2x + 3y \\le 18 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$ là một tam giác'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $x, y$ lần lượt là số ha rau và hoa trồng được ($x \\ge 0, y \\ge 0$). \\\\
            Tổng diện tích trồng không quá $8$ ha nên $x + y \\le 8$. \\\\
            Số công không quá $180$ nên $20x + 30y \\le 180 \\Leftrightarrow 2x + 3y \\le 18$. \\\\
            Ta có hệ bất phương trình: $\\begin{cases} x + y \\le 8 \\\\ 2x + 3y \\le 18 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$. \\\\
            Vẽ các đường thẳng $d_1: x+y=8$, $d_2: 2x+3y=18$ và xác định các nửa mặt phẳng thỏa mãn.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.5, line width=1pt]
            \\draw[->] (-2, 0) -- (10, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 10) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (10,10);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (10,10);
            \\fill[white] (0,0) -- (8,0) -- (6,2) -- (0,6) -- cycle;
            \\draw[black] (-2,10) -- (10,-2); 
            \\draw[black] (-3,8) -- (12,-2);  
            \\draw[black] (0,-2) -- (0,10); 
            \\draw[black] (-2,0) -- (10,0); 
            \\coordinate (A) at (8,0);
            \\coordinate (B) at (6,2);
            \\coordinate (C) at (0,6);
            \\fill (0,0) circle (3pt);
            \\fill (A) circle (3pt) node[above right] {$A$};
            \\fill (B) circle (3pt) node[above right] {$B$};
            \\fill (C) circle (3pt) node[above right] {$C$};
            \\node at (8,0) [below] {$8$};
            \\node at (0,6) [left] {$6$};
            \\draw[dashed] (6,0) node[below] {$6$} -- (6,2) -- (0,2) node[left] {$2$};
            \\end{tikzpicture}
            \\end{center}
            Miền nghiệm là phần mặt phẳng không bị gạch chéo, chính là tứ giác $OABC$ với $O(0;0), A(8;0), B(6;2), C(0;6)$.''')

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
            # Tính giá trị lớn nhất
            max_val = c_x * 6 + c_y * 2

            # Các đáp án
            vdc_da_1_d = '\\True Tiền thu được cao nhất khi $x = 6, y = 2$'
            vdc_da_1_s = 'Tiền thu được cao nhất khi $x = 8, y = 0$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tiền thu được là $T(x;y) = %sx + %sy$. \\\\
            Ta tính giá trị của $T(x;y)$ tại các đỉnh của tứ giác $OABC$: \\\\
            $T(0;0) = 0$ \\\\
            $T(8;0) = %s \\cdot 8 + %s \\cdot 0 = %s$ \\\\
            $T(6;2) = %s \\cdot 6 + %s \\cdot 2 = %s$ \\\\
            $T(0;6) = %s \\cdot 0 + %s \\cdot 6 = %s$ \\\\
            Vì $%s$ là giá trị lớn nhất nên tiền thu được cao nhất khi $x = 6, y = 2$.''' %
            (c_x, c_y,
             c_x, c_y, c_x*8,
             c_x, c_y, max_val,
             c_x, c_y, c_y*6,
             max_val))

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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

