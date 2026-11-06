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


def bt_dang11_p2_b2_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến
            k = random.choice([0, 2, 4, 6])
            X_str = "\\{" + ";".join([str(i+k) for i in range(1, 10)]) + "\\}"
            L_str = "\\{" + ";".join([str(i+k) for i in range(1, 10, 2)]) + "\\}"
            C_str = "\\{" + ";".join([str(i+k) for i in range(2, 9, 2)]) + "\\}"

            c_num = 5 + k
            d_num = 7 + k

            v_L1 = "\\{%s; %s; %s\\}" % (1+k, 3+k, 5+k)
            v_L2 = "\\{%s; %s; %s\\}" % (3+k, 5+k, 7+k)
            v_L3 = "\\{%s; %s; %s\\}" % (5+k, 7+k, 9+k)
            v_L4 = "\\{%s; %s; %s\\}" % (1+k, 5+k, 9+k)

            v_C1 = "\\{%s; %s; %s\\}" % (2+k, 4+k, 6+k)
            v_C2 = "\\{%s; %s; %s\\}" % (4+k, 6+k, 8+k)

            p_L1 = "\\{%s; %s\\}" % (1+k, 9+k)
            p_L2 = "\\{%s; %s\\}" % (3+k, 7+k)
            p_C1 = "\\{%s; %s\\}" % (2+k, 8+k)
            p_C2 = "\\{%s; %s\\}" % (4+k, 6+k)

            d_s1 = "\\{%s; %s; %s\\}" % (1+k, 3+k, 7+k)
            d_s2 = "\\{%s; %s; %s\\}" % (1+k, 5+k, 7+k)
            d_s3 = "\\{%s; %s; %s\\}" % (1+k, 7+k, 9+k)
            d_s4 = "\\{%s; %s; %s\\}" % (3+k, 5+k, 9+k)
            d_s5 = "\\{%s; %s; %s\\}" % (3+k, 7+k, 9+k)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Chọn $6$ số phân biệt từ tập hợp $X = %s$ để xếp vào $6$ ô hình tròn tại các đỉnh $(A;B;C)$ và các trung điểm $(M;N;P)$ của một tam giác như hình vẽ gốc. Gọi $\\Omega$ là tập hợp tất cả các cách xếp sao cho $3$ số trên mỗi cạnh của tam giác luôn lập thành một cấp số cộng. Chọn ngẫu nhiên một cách sắp xếp từ tập $\\Omega$. \\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=1, thick]
            \\coordinate (A) at (0,3);
            \\coordinate (B) at (-1.5,0);
            \\coordinate (C) at (1.5,0);
            \\coordinate (M) at (0,0);
            \\coordinate (P) at (-0.75,1.5);
            \\coordinate (N) at (0.75,1.5);
            \\draw[line width=1pt, color=blue!50!black] (A) -- (B) -- (C) -- cycle;
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (A) circle (0.3) node[black] {$A$};
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (B) circle (0.3) node[black] {$B$};
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (C) circle (0.3) node[black] {$C$};
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (M) circle (0.3) node[black] {$M$};
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (N) circle (0.3) node[black] {$N$};
            \\filldraw[fill=teal!20, draw=red!60, line width=1pt] (P) circle (0.3) node[black] {$P$};
            \\end{tikzpicture}
            \\end{center}''' % (X_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $n(\\Omega) = 48$'
            nb_da_1_s_val = random.choice([36, 60, 24])
            nb_da_1_s = '$n(\\Omega) = %s$' % nb_da_1_s_val
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tập hợp $X = %s$ có tập số lẻ $L = %s$ và tập số chẵn $C = %s$. \\\\
            Với tập số lẻ thì tổng số cách xếp $3$ số vào $3$ đỉnh là $A_5^3$. Các bộ số tạo thành cấp số cộng (các trường hợp vi phạm) có $4$ bộ $%s$, $%s$, $%s$, $%s$. \\\\
            Mỗi bộ có $3!$ cách xếp hoán vị vào $3$ đỉnh nên số trường hợp vi phạm là $4.3! = 24$. \\\\
            Vậy số cách xếp thỏa mãn là $60 - 4.3! = 36$ (cách). \\\\
            Với tập số chẵn thì tổng số cách xếp $3$ số vào $3$ đỉnh là $A_4^3$. Các bộ số tạo thành cấp số cộng là $%s$, $%s$. \\\\
            Mỗi bộ này có $3!$ cách hoán vị vào ba đỉnh nên số trường hợp vi phạm là $2.3!$. \\\\
            Vậy số cách xếp thỏa mãn là $24 - 2.3! = 12$ (cách). \\\\
            Vậy tổng số cách xếp là $n(\\Omega) = 36 + 12 = 48$ (cách).'''
            % (X_str, L_str, C_str, v_L1, v_L2, v_L3, v_L4, v_C1, v_C2))

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
            th_da_1_d = '\\True Xác suất để ba số ở các đỉnh $(A;B;C)$ đều là số chẵn bằng $0,25$'
            th_da_1_s = 'Xác suất để ba số ở các đỉnh $(A;B;C)$ đều là số chẵn bằng $0,5$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Với tập số chẵn thì tổng số cách xếp $3$ số vào $3$ đỉnh là $A_4^3$. Các bộ số tạo thành cấp số cộng là $%s$, $%s$. \\\\
            Mỗi bộ này có $3!$ cách hoán vị vào ba đỉnh nên số trường hợp vi phạm là $2.3!$. \\\\
            Vậy số cách xếp thỏa mãn là $n(B) = 24 - 2.3! = 12$ (cách). \\\\
            Xác suất để ba số ở các đỉnh $(A;B;C)$ đều là số chẵn là: $P = \\frac{12}{48} = 0,25$.'''
            % (v_C1, v_C2))

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
            vd_da_1_d = '\\True Xác suất để chữ số $%s$ nằm ở vị trí trung điểm bằng $0,75$' % c_num
            vd_da_1_s = 'Xác suất để chữ số $%s$ nằm ở vị trí trung điểm bằng $0,65$' % c_num
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Trường hợp đỉnh lẻ gồm $5$ số $L = %s$ thì để $A+B=%s$ với $A, B$ là số lẻ thì ta có hai cặp là $%s$ và $%s$. \\\\
            Cặp $%s$ có $2!$ (cách xếp) vào $A, B$, còn lại các số $\\{%s; %s; %s\\}$ (loại $%s$ do đã dùng ở $P$) nên $C$ chỉ có thể là $%s$ hoặc $%s$ nên có $2$ cách nên số cách là $2.2 = 4$ (cách). \\\\
            Cặp $%s$ có $2!$ (cách xếp) vào $A, B$, còn lại các số $\\{%s; %s; %s\\}$ (loại $%s$ do đã dùng ở $P$) nên $C$ chỉ có thể là $%s$ hoặc $%s$ nên có $2$ cách nên số cách là $2.2 = 4$ (cách). \\\\
            Vậy tổng trường hợp thỏa mãn cho số lẻ là: $4 + 4 = 8$ (cách). \\\\
            Trường hợp đỉnh chẵn gồm $4$ số $C = %s$ thì để $A+B=%s$ với $A, B$ là số chẵn thì ta có hai cặp là $%s$ và $%s$. \\\\
            Cặp $%s$ có $2!$ (cách xếp) vào $A, B$, còn lại các số $\\{%s; %s\\}$ nên $C$ chỉ có thể là $%s$ hoặc $%s$ nên có $2$ cách nên số cách là $2.2 = 4$ (cách). \\\\
            Cặp $%s$ thì $C$ phải là $%s$ hoặc $%s$. \\\\
            Nếu $C = %s$ thì bộ $\\{%s; %s; %s\\}$ vi phạm vì nó tạo thành cấp số cộng ở đỉnh. \\\\
            Nếu $C = %s$ thì bộ $\\{%s; %s; %s\\}$ vi phạm vì nó tạo thành cấp số cộng ở đỉnh. \\\\
            Vậy tổng trường hợp thỏa mãn cho số chẵn là: $4 + 0 = 4$ (cách). \\\\
            Vì có ba vị trí trung điểm $(M, N, P)$ là như nhau nên ta có $n(C) = 3.12 = 36$ (cách). \\\\
            Xác suất để chữ số $%s$ nằm ở vị trí trung điểm là: $P = \\frac{n(C)}{n(\\Omega)} = \\frac{36}{48} = 0,75$.'''
            % (L_str, 2*c_num, p_L1, p_L2,
               p_L1, 3+k, 5+k, 7+k, c_num, 3+k, 7+k,
               p_L2, 1+k, 5+k, 9+k, c_num, 1+k, 9+k,
               C_str, 2*c_num, p_C1, p_C2,
               p_C1, 4+k, 6+k, 4+k, 6+k,
               p_C2, 2+k, 8+k,
               2+k, 4+k, 6+k, 2+k,
               8+k, 4+k, 6+k, 8+k,
               c_num))

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
            vdc_da_1_d = '\\True Biết rằng ba số ở các đỉnh đều là số lẻ thì xác suất để chữ số $%s$ có mặt trong cách sắp xếp đó bằng $0,83$ (Kết quả làm tròn đến hàng phần trăm)' % d_num
            vdc_da_1_s = 'Biết rằng ba số ở các đỉnh đều là số lẻ thì xác suất để chữ số $%s$ có mặt trong cách sắp xếp đó bằng $0,67$ (Kết quả làm tròn đến hàng phần trăm)' % d_num
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ba số ở các đỉnh đều là đỉnh lẻ nên $n(\\Omega_D) = 36$. \\\\
            Số bộ đỉnh lẻ có chứa số $%s$ (ở đỉnh hoặc trung điểm là): $%s$, $%s$, $%s$, $%s$, $%s$. \\\\
            Có $5$ bộ chứa số $%s$ nên số cách sắp xếp thuận lợi là: $n(D) = 5.6 = 30$ (cách). \\\\
            Xác suất cần tính $P = \\frac{n(D)}{n(\\Omega_D)} = \\frac{30}{36} = \\frac{5}{6} \\approx 0,83$.'''
            % (d_num, d_s1, d_s2, d_s3, d_s4, d_s5, d_num))

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
                str(noidungcauhoi)+ '\n' +
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

