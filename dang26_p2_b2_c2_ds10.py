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


def bt_dang26_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và random thông số
            P_x = random.choice([500, 600, 700])
            P_y = random.choice([350, 400, 450, 500])

            # Tính giá trị tại các đỉnh
            val_A = P_x * 4 + P_y * 14
            val_B = P_x * 8 + P_y * 12
            val_C = P_x * 16

            # Tính giá trị lớn nhất
            M_val = max(val_A, val_B, val_C)
            M_str = str(M_val * 1000)
            M_str_false = str((M_val + random.choice([200, -200, 500])) * 1000)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một xưởng sản xuất bàn và ghế. Một chiếc bàn cần $1,5$ giờ lắp ráp và $1$ giờ hoàn thiện; một chiếc ghế cần $1$ giờ lắp ráp và $2$ giờ hoàn thiện. Bộ phận lắp ráp có $3$ nhân công, bộ phận hoàn thiện có $4$ nhân công. Biết thị trường luôn tiêu thụ hết sản phẩm của xưởng và lượng ghế tiêu thụ không vượt quá $3,5$ lần số bàn; một nhân công làm việc không quá $8$ tiếng mỗi ngày; một chiếc bàn lãi $%s$ nghìn đồng, một chiếc ghế lãi $%s$ nghìn đồng. Gọi $x, y$ ($x, y \\in \\mathbb{N}$) lần lượt là số bàn, số ghế mà xưởng sản xuất trong một ngày.''' % (P_x, P_y))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Bất phương trình mô tả số giờ lắp ráp bàn và ghế trong một ngày của các nhân công là $1,5x + y \\le 24$'
            nb_da_1_s = 'Bất phương trình mô tả số giờ lắp ráp bàn và ghế trong một ngày của các nhân công là $x + 1,5y \\le 24$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Bộ phận lắp ráp có $3$ nhân công, mỗi nhân công làm việc không quá $8$ tiếng mỗi ngày nên tổng thời gian lắp ráp tối đa là $3 \\cdot 8 = 24$ (giờ). \\\\
            Thời gian để lắp ráp $x$ chiếc bàn và $y$ chiếc ghế là $1,5x + y$ (giờ). \\\\
            Suy ra bất phương trình mô tả số giờ lắp ráp là $1,5x + y \\le 24$.''')

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
            th_da_1_d = '\\True Bất phương trình mô tả số giờ hoàn thiện bàn và ghế trong một ngày của các nhân công là $x + 2y \\le 32$'
            th_da_1_s = 'Bất phương trình mô tả số giờ hoàn thiện bàn và ghế trong một ngày của các nhân công là $2x + y \\le 32$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Bộ phận hoàn thiện có $4$ nhân công, mỗi nhân công làm việc không quá $8$ tiếng mỗi ngày nên tổng thời gian hoàn thiện tối đa là $4 \\cdot 8 = 32$ (giờ). \\\\
            Thời gian để hoàn thiện $x$ chiếc bàn và $y$ chiếc ghế là $1 \\cdot x + 2 \\cdot y = x + 2y$ (giờ). \\\\
            Suy ra bất phương trình mô tả số giờ hoàn thiện là $x + 2y \\le 32$.''')

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
            vd_da_1_d = '\\True Hệ bất phương trình mô tả số lượng bàn và ghế mà trong một ngày phân xưởng có thể sản xuất là $\\begin{cases} 1,5x + y \\le 24 \\\\ x + 2y \\le 32 \\\\ 3,5x - y \\ge 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$'
            vd_da_1_s = 'Hệ bất phương trình mô tả số lượng bàn và ghế mà trong một ngày phân xưởng có thể sản xuất là $\\begin{cases} 1,5x + y \\le 24 \\\\ x + 2y \\le 32 \\\\ 3,5x - y \\le 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Lượng ghế tiêu thụ không vượt quá $3,5$ lần số bàn nên ta có bất phương trình $y \\le 3,5x \\Leftrightarrow 3,5x - y \\ge 0$. \\\\
            Vì $x, y \\in \\mathbb{N}$ nên $x \\ge 0, y \\ge 0$. \\\\
            Kết hợp với các điều kiện ở trên, ta có hệ bất phương trình: \\\\
            $\\begin{cases} 1,5x + y \\le 24 \\\\ x + 2y \\le 32 \\\\ 3,5x - y \\ge 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$.''')

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
            vdc_da_1_d = '\\True Tiền lãi cao nhất mà xưởng có thể thu được trong một ngày là $%s$ đồng' % (M_str)
            vdc_da_1_s = 'Tiền lãi cao nhất mà xưởng có thể thu được trong một ngày là $%s$ đồng' % (M_str_false)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số tiền lãi xưởng thu được trong một ngày là $F(x;y) = %sx + %sy$ (nghìn đồng). \\\\
            Bài toán đưa về tìm giá trị lớn nhất của biểu thức $F(x;y)$ trên miền nghiệm của hệ bất phương trình: \\\\
            $\\begin{cases} 1,5x + y \\le 24 \\\\ x + 2y \\le 32 \\\\ 3,5x - y \\ge 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.3, line width=1pt]
            \\draw[->] (-2, 0) -- (20, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 18) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (20,18);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (20,18);
            \\fill[white] (0,0) -- (4,14) -- (8,12) -- (16,0) -- cycle;
            \\draw[black] (-2, 27) -- (18, -3); 
            \\draw[black] (-2, 17) -- (20, 6);  
            \\draw[black] (-1, -3.5) -- (6, 21); 
            \\draw[black] (0, 0) -- (20, 0); 
            \\draw[black] (0, -2) -- (0, 18);
            \\coordinate (A) at (4,14);
            \\coordinate (B) at (8,12);
            \\coordinate (C) at (16,0);
            \\fill (0,0) circle (3.5pt);
            \\fill (A) circle (3.5pt) node[above left] {$A(4;14)$};
            \\fill (B) circle (3.5pt) node[above right] {$B(8;12)$};
            \\fill (C) circle (3.5pt) node[above right] {$C(16;0)$};
            \\end{tikzpicture}
            \\end{center}
            Miền nghiệm là tứ giác $OABC$ với các đỉnh $O(0;0), A(4;14), B(8;12), C(16;0)$. \\\\
            Tính giá trị của $F(x;y)$ tại các đỉnh: \\\\
            $F(0;0) = 0$ \\\\
            $F(4;14) = %s \\cdot 4 + %s \\cdot 14 = %s$ \\\\
            $F(8;12) = %s \\cdot 8 + %s \\cdot 12 = %s$ \\\\
            $F(16;0) = %s \\cdot 16 + %s \\cdot 0 = %s$ \\\\
            Quan sát các kết quả, ta thấy giá trị lớn nhất là $%s$. Do đó tiền lãi cao nhất xưởng thu được là $%s$ đồng.''' % (P_x, P_y, P_x, P_y, val_A, P_x, P_y, val_B, P_x, P_y, val_C, M_val, M_str))

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

