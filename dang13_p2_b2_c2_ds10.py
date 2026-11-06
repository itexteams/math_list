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


def bt_dang13_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            # Random điểm cho câu Thông hiểu
            list_pt_true = [(2, 2), (2, 3), (3, 1), (4, 1)]
            list_pt_false = [(4, 3), (0, 0), (6, 6)]
            pt_t = random.choice(list_pt_true)
            pt_f = random.choice(list_pt_false)

            # Random hàm số F cho câu Vận dụng cao
            # Chọn m, n sao cho F đạt Min tại C(1;5) hoặc B(5;1) để luôn có x0^2 + y0^2 = 26
            list_F = [(4, -5), (-3, 2), (2, -4)] 
            m, n = random.choice(list_F)
            f_str = "%sx %s %sy" % (m, "+" if n > 0 else "-", abs(n))

            # Tính giá trị F tại các đỉnh
            val_A = m*3 + n*0
            val_B = m*5 + n*1
            val_C = m*1 + n*5
            val_D_num = m*3 + n*4
            val_D_str = "\\frac{%s}{3}" % val_D_num
            if val_D_num % 3 == 0:
                val_D_str = "%s" % (val_D_num // 3)

            min_val = min(val_A, val_B, val_C, val_D_num / 3.0)

            if min_val == val_C:
                min_pt = "C(1;5)"
                min_val_str = "%s" % val_C
            elif min_val == val_B:
                min_pt = "B(5;1)"
                min_val_str = "%s" % val_B

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình: $\\begin{cases} 2x + 3y \\ge 6 \\\\ x - 2y \\le 3 \\\\ x + y \\le 6 \\\\ x \\ge 1 \\end{cases} (I)$.''')

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True Hệ bất phương trình $(I)$ là hệ bất phương trình bậc nhất hai ẩn $x; y$'
            nb_da_1_s = 'Hệ bất phương trình $(I)$ là hệ bất phương trình bậc nhất một ẩn $x$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hệ bất phương trình $(I)$ chứa hai ẩn $x, y$ với bậc cao nhất của các ẩn là $1$, nên nó là hệ bất phương trình bậc nhất hai ẩn.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu 
            ########################################################################
            th_da_1_d = '\\True Cặp số $(x; y) = (%s; %s)$ là một nghiệm của hệ bất phương trình trên' % (pt_t[0], pt_t[1])
            th_da_1_s = 'Cặp số $(x; y) = (%s; %s)$ là một nghiệm của hệ bất phương trình trên' % (pt_f[0], pt_f[1])
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Thay tọa độ điểm vào hệ bất phương trình $(I)$ ta kiểm tra được tính đúng sai của mệnh đề.''')
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng 
            ########################################################################
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình $(I)$ là miền tứ giác'
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình $(I)$ là miền tam giác'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Vẽ các đường thẳng tương ứng với các phương trình trên mặt phẳng tọa độ.\\\\
            Miền nghiệm của hệ $(I)$ là phần mặt phẳng không bị gạch chéo trong hình vẽ bên dưới (bao gồm cả biên). \\\\
            Nhìn vào đồ thị ta thấy miền nghiệm là một tứ giác với các đỉnh $A(3;0)$, $B(5;1)$, $C(1;5)$, $D\\left(1;\\frac{4}{3}\\right)$.\\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]
            \\draw[->] (-2.5,0) -- (6.5,0) node[below] {$x$};
            \\draw[->] (0,-1.5) -- (0,6) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2.5,-1.5) rectangle (6.5,6);
            \\fill[pattern=north east lines, pattern color=black] (-2.5,-1.5) rectangle (6.5,6);
            \\fill[white] (1, 4/3) -- (3, 0) -- (5, 1) -- (1, 5) -- cycle;
            \\draw[->] (-2.5,0) -- (6.5,0);
            \\draw[->] (0,-1.5) -- (0,6);
            \\draw[black] (-2.5, {11/3}) -- (6.5, {-7/3});
            \\draw[black] (-2.5, {-11/4}) -- (6.5, {7/4});
            \\draw[black] (-2.5, 8.5) -- (6.5, -0.5);
            \\draw[black] (1, -1.5) -- (1, 6);
            \\coordinate (A) at (3,0);
            \\coordinate (B) at (5,1);
            \\coordinate (C) at (1,5);
            \\coordinate (D) at (1,1.3333);
            \\node at (A) [above right] {$A$};
            \\node at (B) [above] {$B$};
            \\node at (C) [right] {$C$};
            \\node at (D) [right] {$D$};
            \\end{tikzpicture}
            \\end{center}''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao 
            ########################################################################
            vdc_da_1_d = '\\True Nếu $x = x_0; y = y_0$ là nghiệm của hệ bất phương trình sao cho $F = %s$ đạt giá trị nhỏ nhất thì $x_0^2 + y_0^2 = 26$' % (f_str)
            vdc_da_1_s = 'Nếu $x = x_0; y = y_0$ là nghiệm của hệ bất phương trình sao cho $F = %s$ đạt giá trị nhỏ nhất thì $x_0^2 + y_0^2 = 16$' % (f_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta tính giá trị của biểu thức $F = %s$ tại các đỉnh của tứ giác $ABCD$: \\\\
            Tại $A(3;0) \\Rightarrow F = %s$. \\\\
            Tại $B(5;1) \\Rightarrow F = %s$. \\\\
            Tại $C(1;5) \\Rightarrow F = %s$. \\\\
            Tại $D\\left(1;\\frac{4}{3}\\right) \\Rightarrow F = %s$. \\\\
            Suy ra giá trị nhỏ nhất của $F$ là $%s$ đạt được tại $(x_0; y_0)$ là toạ độ của điểm $%s$. \\\\
            Khi đó, $x_0^2 + y_0^2 = 26$.''' % (f_str, val_A, val_B, val_C, val_D_str, min_val_str, min_pt))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

